/**
 * Study Tracker - Preload Script
 * Exposes safe IPC methods to the renderer process
 */

const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    // Settings
    updateSettings: (settings) => ipcRenderer.invoke('update-settings', settings),
    
    // Timer state notification
    timerStateChanged: (state) => ipcRenderer.invoke('timer-state-changed', state),
    
    // Window controls
    minimizeWindow: () => ipcRenderer.invoke('minimize-window'),
    closeWindow: () => ipcRenderer.invoke('close-window'),
    
    // Platform info
    isElectron: true
});
