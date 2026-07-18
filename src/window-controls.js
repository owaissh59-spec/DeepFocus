/**
 * Window Controls - Minimize, Maximize, Fullscreen, Close
 * Works with Tauri (native) and fallback for browser/PWA (Web Fullscreen API)
 */

(function() {
    let isFullscreen = false;
    let isTauri = !!window.__TAURI__;

    // Minimize
    document.getElementById('btn-minimize').addEventListener('click', async () => {
        if (isTauri) {
            const { getCurrentWindow } = window.__TAURI__.window;
            await getCurrentWindow().minimize();
        }
    });

    // Maximize / Restore
    document.getElementById('btn-maximize').addEventListener('click', async () => {
        if (isTauri) {
            const win = window.__TAURI__.window.getCurrentWindow();
            const maximized = await win.isMaximized();
            if (maximized) {
                await win.unmaximize();
            } else {
                await win.maximize();
            }
        } else {
            // Browser fallback - toggle between normal and large
            toggleFullscreen();
        }
    });

    // Fullscreen (hides taskbar)
    document.getElementById('btn-fullscreen').addEventListener('click', () => {
        toggleFullscreen();
    });

    // Close (hide window, keep running)
    document.getElementById('btn-close').addEventListener('click', async () => {
        if (isTauri) {
            const win = window.__TAURI__.window.getCurrentWindow();
            await win.hide();
        } else {
            // Browser - just minimize
            window.close();
        }
    });

    // Toggle fullscreen
    async function toggleFullscreen() {
        if (isTauri) {
            const win = window.__TAURI__.window.getCurrentWindow();
            const fs = await win.isFullscreen();
            await win.setFullscreen(!fs);
            isFullscreen = !fs;
            document.body.classList.toggle('fullscreen', isFullscreen);
        } else {
            // Web Fullscreen API
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen();
                isFullscreen = true;
                document.body.classList.add('fullscreen');
            } else {
                document.exitFullscreen();
                isFullscreen = false;
                document.body.classList.remove('fullscreen');
            }
        }
    }

    // ESC to exit fullscreen
    document.addEventListener('keydown', async (e) => {
        if (e.key === 'Escape' && isFullscreen) {
            if (isTauri) {
                const win = window.__TAURI__.window.getCurrentWindow();
                await win.setFullscreen(false);
                isFullscreen = false;
                document.body.classList.remove('fullscreen');
            }
            // Browser handles ESC automatically for fullscreen API
        }
        // F11 to toggle fullscreen
        if (e.key === 'F11') {
            e.preventDefault();
            toggleFullscreen();
        }
    });

    // Listen for browser fullscreen change
    document.addEventListener('fullscreenchange', () => {
        if (!document.fullscreenElement) {
            isFullscreen = false;
            document.body.classList.remove('fullscreen');
        }
    });

    // Double-click titlebar to maximize
    document.querySelector('.titlebar').addEventListener('dblclick', async (e) => {
        if (e.target.closest('.titlebar-buttons')) return;
        if (isTauri) {
            const win = window.__TAURI__.window.getCurrentWindow();
            const maximized = await win.isMaximized();
            if (maximized) await win.unmaximize();
            else await win.maximize();
        }
    });
})();
