/**
 * Study Tracker - Electron Main Process
 * Handles window management, always-on-top, auto-start, system tray, power management
 */

const { app, BrowserWindow, Tray, Menu, ipcMain, powerSaveBlocker, nativeImage, screen } = require('electron');
const path = require('path');

// Single instance lock - prevent multiple instances
const gotTheLock = app.requestSingleInstanceLock();
if (!gotTheLock) {
    app.quit();
    process.exit(0);
}

let mainWindow = null;
let tray = null;
let powerSaveId = null;
let isQuitting = false;

// Settings defaults
let settings = {
    alwaysOnTop: true,
    autoStart: true
};

// ============================================
// WINDOW CREATION
// ============================================

function createWindow() {
    const primaryDisplay = screen.getPrimaryDisplay();
    const { width, height } = primaryDisplay.workAreaSize;

    mainWindow = new BrowserWindow({
        width: 400,
        height: 780,
        minWidth: 340,
        minHeight: 600,
        x: width - 420,  // Position at right side of screen
        y: 20,
        frame: false,
        transparent: false,
        alwaysOnTop: settings.alwaysOnTop,
        skipTaskbar: false,
        resizable: true,
        backgroundColor: '#000000',
        icon: path.join(__dirname, 'icons', 'icon.png'),
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, 'preload.js')
        },
        // Lockscreen-like appearance
        titleBarStyle: 'hidden',
        titleBarOverlay: false
    });

    mainWindow.loadFile(path.join(__dirname, 'index.html'));

    // Prevent window from closing - minimize to tray instead
    mainWindow.on('close', (event) => {
        if (!isQuitting) {
            event.preventDefault();
            mainWindow.hide();
            return false;
        }
    });

    mainWindow.on('closed', () => {
        mainWindow = null;
    });

    // Remove menu bar
    mainWindow.setMenuBarVisibility(false);

    // Make window draggable from anywhere (lockscreen feel)
    mainWindow.webContents.on('did-finish-load', () => {
        mainWindow.webContents.insertCSS(`
            body { -webkit-app-region: drag; }
            button, input, .icon-btn, .fab, .fab-small, .control-btn, .history-list, .modal, a { -webkit-app-region: no-drag; }
        `);
    });
}

// ============================================
// SYSTEM TRAY
// ============================================

function createTray() {
    // Create a simple tray icon (16x16 green circle for active)
    const iconPath = path.join(__dirname, 'icons', 'tray-icon.png');
    
    // Try to load icon, fall back to creating one programmatically
    let trayIcon;
    try {
        trayIcon = nativeImage.createFromPath(iconPath);
        if (trayIcon.isEmpty()) {
            trayIcon = createTrayIcon();
        }
    } catch (e) {
        trayIcon = createTrayIcon();
    }

    tray = new Tray(trayIcon);
    tray.setToolTip('DeepFocus');

    const contextMenu = Menu.buildFromTemplate([
        {
            label: 'Show DeepFocus',
            click: () => {
                if (mainWindow) {
                    mainWindow.show();
                    mainWindow.focus();
                }
            }
        },
        { type: 'separator' },
        {
            label: 'Always on Top',
            type: 'checkbox',
            checked: settings.alwaysOnTop,
            click: (menuItem) => {
                settings.alwaysOnTop = menuItem.checked;
                if (mainWindow) {
                    mainWindow.setAlwaysOnTop(menuItem.checked);
                }
            }
        },
        { type: 'separator' },
        {
            label: 'Quit',
            click: () => {
                isQuitting = true;
                app.quit();
            }
        }
    ]);

    tray.setContextMenu(contextMenu);

    tray.on('double-click', () => {
        if (mainWindow) {
            mainWindow.show();
            mainWindow.focus();
        }
    });
}

function createTrayIcon() {
    // Create a simple 16x16 icon programmatically
    const size = 16;
    const canvas = Buffer.alloc(size * size * 4);
    
    // Draw a green circle
    for (let y = 0; y < size; y++) {
        for (let x = 0; x < size; x++) {
            const dx = x - size / 2;
            const dy = y - size / 2;
            const dist = Math.sqrt(dx * dx + dy * dy);
            const idx = (y * size + x) * 4;
            
            if (dist < size / 2 - 1) {
                canvas[idx] = 0;      // R
                canvas[idx + 1] = 230; // G
                canvas[idx + 2] = 118; // B
                canvas[idx + 3] = 255; // A
            } else {
                canvas[idx + 3] = 0; // transparent
            }
        }
    }
    
    return nativeImage.createFromBuffer(canvas, { width: size, height: size });
}

// ============================================
// POWER MANAGEMENT
// ============================================

function startPowerSaveBlock() {
    if (powerSaveId === null) {
        // Prevent display sleep while timer is running
        powerSaveId = powerSaveBlocker.start('prevent-display-sleep');
    }
}

function stopPowerSaveBlock() {
    if (powerSaveId !== null) {
        powerSaveBlocker.stop(powerSaveId);
        powerSaveId = null;
    }
}

// ============================================
// AUTO-START CONFIGURATION
// ============================================

function setAutoStart(enabled) {
    app.setLoginItemSettings({
        openAtLogin: enabled,
        path: app.getPath('exe'),
        args: ['--hidden']
    });
}

// ============================================
// IPC HANDLERS (communication with renderer)
// ============================================

function setupIPC() {
    // Settings update from renderer
    ipcMain.handle('update-settings', (event, newSettings) => {
        if (newSettings.alwaysOnTop !== undefined) {
            settings.alwaysOnTop = newSettings.alwaysOnTop;
            if (mainWindow) {
                mainWindow.setAlwaysOnTop(settings.alwaysOnTop);
            }
        }
        if (newSettings.autoStart !== undefined) {
            settings.autoStart = newSettings.autoStart;
            setAutoStart(settings.autoStart);
        }
    });

    // Timer state changes - manage power saving
    ipcMain.handle('timer-state-changed', (event, state) => {
        if (state === 'running') {
            startPowerSaveBlock();
            if (tray) tray.setToolTip('DeepFocus - Studying...');
        } else if (state === 'paused') {
            stopPowerSaveBlock();
            if (tray) tray.setToolTip('DeepFocus - On Break');
        } else {
            stopPowerSaveBlock();
            if (tray) tray.setToolTip('DeepFocus');
        }
    });

    // Window controls
    ipcMain.handle('minimize-window', () => {
        if (mainWindow) mainWindow.minimize();
    });

    ipcMain.handle('close-window', () => {
        if (mainWindow) mainWindow.hide();
    });
}

// ============================================
// APP LIFECYCLE
// ============================================

app.whenReady().then(() => {
    createWindow();
    createTray();
    setupIPC();

    // Set auto-start on first run
    setAutoStart(settings.autoStart);

    // Handle --hidden flag (start minimized to tray)
    if (process.argv.includes('--hidden')) {
        mainWindow.hide();
    }
});

// Second instance - show the existing window
app.on('second-instance', () => {
    if (mainWindow) {
        if (mainWindow.isMinimized()) mainWindow.restore();
        mainWindow.show();
        mainWindow.focus();
    }
});

app.on('window-all-closed', () => {
    // Don't quit on window close - keep in tray
    if (process.platform !== 'darwin') {
        // Only quit if explicitly quitting
        if (isQuitting) {
            app.quit();
        }
    }
});

app.on('activate', () => {
    if (mainWindow === null) {
        createWindow();
    } else {
        mainWindow.show();
    }
});

app.on('before-quit', () => {
    isQuitting = true;
    stopPowerSaveBlock();
});
