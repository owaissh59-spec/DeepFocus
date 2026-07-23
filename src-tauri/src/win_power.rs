// Windows-only power / lock-screen integration for DeepFocus.
//
// Purpose: replicate (as far as the Windows OS allows) the Android
// "always-on display" behaviour, where the study timer stays lit while a
// session is active and re-appears when the display/lock returns.
//
// Two things happen here:
//   1. While a session is running we ask Windows to keep the display and the
//      system awake (SetThreadExecutionState). This stops the screen from
//      idling off / the machine from idle-sleeping, so the timer stays lit.
//   2. We subclass the main window's WndProc to listen for:
//        - WM_WTSSESSION_CHANGE  -> workstation unlock
//        - WM_POWERBROADCAST     -> console display turned back ON
//      When either fires *and* a session is active, we show + focus the
//      window and call window.enterAOD() so the lit timer re-appears.
//
// NOTE: Windows does not allow any third-party app to render on the secure
// lock screen, and an app cannot wake the machine from a real Sleep (S3 /
// Modern Standby). Those are OS limitations, not bugs in this code.

use std::sync::atomic::{AtomicBool, AtomicIsize, Ordering};
use std::sync::OnceLock;

use tauri::{AppHandle, Manager};

use windows_sys::core::GUID;
use windows_sys::Win32::Foundation::{HANDLE, HWND, LPARAM, LRESULT, WPARAM};
use windows_sys::Win32::System::Power::{
    RegisterPowerSettingNotification, SetThreadExecutionState, ES_CONTINUOUS,
    ES_DISPLAY_REQUIRED, ES_SYSTEM_REQUIRED,
};
use windows_sys::Win32::System::RemoteDesktop::WTSRegisterSessionNotification;
use windows_sys::Win32::UI::WindowsAndMessaging::{
    CallWindowProcW, DefWindowProcW, SetWindowLongPtrW, WNDPROC,
};

// --- Constants defined locally to stay independent of windows-sys versions ---
const GWLP_WNDPROC: i32 = -4;
const WM_POWERBROADCAST: u32 = 0x0218;
const WM_WTSSESSION_CHANGE: u32 = 0x02B1;
const PBT_POWERSETTINGCHANGE: u32 = 0x8013;
const WTS_SESSION_UNLOCK: u32 = 0x8;
const NOTIFY_FOR_THIS_SESSION: u32 = 0;
const DEVICE_NOTIFY_WINDOW_HANDLE: u32 = 0;

// GUID_CONSOLE_DISPLAY_STATE {6FE69556-704A-47A0-8F24-C28D936FDA47}
const GUID_CONSOLE_DISPLAY_STATE: GUID = GUID {
    data1: 0x6FE6_9556,
    data2: 0x704A,
    data3: 0x47A0,
    data4: [0x8F, 0x24, 0xC2, 0x8D, 0x93, 0x6F, 0xDA, 0x47],
};

#[repr(C)]
struct PowerBroadcastSetting {
    power_setting: GUID,
    data_length: u32,
    data: [u8; 1],
}

static ORIGINAL_WNDPROC: AtomicIsize = AtomicIsize::new(0);
static SESSION_ACTIVE: AtomicBool = AtomicBool::new(false);
static APP_HANDLE: OnceLock<AppHandle> = OnceLock::new();

/// Called from the JS bridge (via the `set_session_active` command) whenever a
/// study session starts (`true`) or stops/pauses (`false`).
pub fn set_session_active(active: bool) {
    SESSION_ACTIVE.store(active, Ordering::SeqCst);

    // SetThreadExecutionState is per-thread and only persists while the calling
    // thread is alive, so always run it on the long-lived main (event-loop)
    // thread rather than a transient command worker thread.
    if let Some(app) = APP_HANDLE.get() {
        let _ = app.run_on_main_thread(move || unsafe {
            if active {
                SetThreadExecutionState(
                    ES_CONTINUOUS | ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED,
                );
            } else {
                SetThreadExecutionState(ES_CONTINUOUS);
            }
        });
    }
}

/// Install the WndProc subclass + register for session / display notifications.
/// Call once during Tauri setup.
pub fn init(app: &AppHandle) {
    let _ = APP_HANDLE.set(app.clone());

    if let Some(window) = app.get_webview_window("main") {
        if let Ok(hwnd) = window.hwnd() {
            // Tauri's HWND wraps a raw handle; cast it to the windows-sys HWND.
            let h = hwnd.0 as HWND;
            unsafe {
                let orig = SetWindowLongPtrW(h, GWLP_WNDPROC, subclass_proc as usize as isize);
                ORIGINAL_WNDPROC.store(orig, Ordering::SeqCst);

                // Lock / unlock notifications.
                let _ = WTSRegisterSessionNotification(h, NOTIFY_FOR_THIS_SESSION);

                // Display on/off notifications (power button -> display off, etc.).
                let _ = RegisterPowerSettingNotification(
                    h as HANDLE,
                    &GUID_CONSOLE_DISPLAY_STATE,
                    DEVICE_NOTIFY_WINDOW_HANDLE,
                );
            }
        }
    }
}

/// Bring the window forward and light up the timer, but only while a session
/// is actually running (matches the Android "only when active" behaviour).
fn wake_lit_timer() {
    if !SESSION_ACTIVE.load(Ordering::SeqCst) {
        return;
    }
    if let Some(app) = APP_HANDLE.get() {
        if let Some(win) = app.get_webview_window("main") {
            let w = win.clone();
            let _ = app.run_on_main_thread(move || {
                let _ = w.unminimize();
                let _ = w.show();
                let _ = w.set_focus();
                let _ = w.eval("window.enterAOD && window.enterAOD();");
            });
        }
    }
}

unsafe extern "system" fn subclass_proc(
    hwnd: HWND,
    msg: u32,
    wparam: WPARAM,
    lparam: LPARAM,
) -> LRESULT {
    match msg {
        WM_WTSSESSION_CHANGE => {
            if wparam as u32 == WTS_SESSION_UNLOCK {
                wake_lit_timer();
            }
        }
        WM_POWERBROADCAST => {
            if wparam as u32 == PBT_POWERSETTINGCHANGE && lparam != 0 {
                let setting = &*(lparam as *const PowerBroadcastSetting);
                // Data: 0 = display off, 1 = display on, 2 = dimmed.
                if guids_equal(&setting.power_setting, &GUID_CONSOLE_DISPLAY_STATE)
                    && setting.data[0] == 1
                {
                    wake_lit_timer();
                }
            }
        }
        _ => {}
    }

    // Forward everything to the window's original procedure.
    let orig = ORIGINAL_WNDPROC.load(Ordering::SeqCst);
    if orig != 0 {
        let proc: WNDPROC = std::mem::transmute::<isize, WNDPROC>(orig);
        CallWindowProcW(proc, hwnd, msg, wparam, lparam)
    } else {
        DefWindowProcW(hwnd, msg, wparam, lparam)
    }
}

fn guids_equal(a: &GUID, b: &GUID) -> bool {
    a.data1 == b.data1 && a.data2 == b.data2 && a.data3 == b.data3 && a.data4 == b.data4
}
