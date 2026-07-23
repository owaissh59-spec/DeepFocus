#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

#[cfg(windows)]
mod win_power;

/// Reported from the web UI whenever a study session starts (`true`) or
/// stops/pauses (`false`). On Windows this keeps the display awake and lets the
/// native layer re-show the lit timer when the screen/lock returns.
#[tauri::command]
fn set_session_active(active: bool) {
    #[cfg(windows)]
    win_power::set_session_active(active);
    #[cfg(not(windows))]
    let _ = active;
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![set_session_active])
        .setup(|_app| {
            #[cfg(windows)]
            win_power::init(_app.handle());
            Ok(())
        })
        .on_window_event(|window, event| {
            // Minimize to taskbar on close instead of quitting
            if let tauri::WindowEvent::CloseRequested { api, .. } = event {
                let _ = window.hide();
                api.prevent_close();
            }
        })
        .run(tauri::generate_context!())
        .expect("error while running DeepFocus");
}
