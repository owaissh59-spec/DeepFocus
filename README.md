# DeepFocus

A minimal, always-on study time tracker with a lockscreen-style dark display. Built for students who want to know exactly how much they study each day.

## Features

- **Precise Timer** - Start, pause, resume with second-level counting
- **Always-on AMOLED Display** - Pure black theme, minimal power draw
- **Crash Recovery** - State persists every second; auto-recovers after shutdown (up to 30 min)
- **Auto-Start** - Launches silently on system boot
- **System Tray** - Runs in background, always accessible
- **Circular Progress Ring** - Dynamically sized, fills as you approach your daily goal
- **Daily Goal** - Customizable target (default 6 hours)
- **Analytics** - Weekly chart, streak counter, daily averages, full session history
- **Break Reminders** - Configurable alerts to rest your eyes
- **Cross-Platform** - Windows (Electron) + Android (PWA)
- **Always on Top** - Stays visible like a lockscreen widget

## Quick Start

```bash
cd DeepFocus
npm install
npm start
```

Or double-click `start.bat`.

## Android (PWA)

1. Host the `src/` folder on any server (e.g. `npx serve src/`)
2. Open in Chrome on your phone
3. Tap "Add to Home Screen"
4. Works offline with screen wake lock

## How It Works

| Action | What Happens |
|--------|-------------|
| **Start** | Begin studying, timer counts up |
| **Pause** | Take a break, session is saved |
| **Resume** | Continue after break |
| **End Day** | Save all data, reset for tomorrow |

Data is stored locally (IndexedDB + localStorage). Nothing is sent anywhere.

## Building

```bash
npm run build:win
```

Creates a Windows installer in `dist/`.

## Project Structure

```
DeepFocus/
├── src/
│   ├── main.js         # Electron (window, tray, power, auto-start)
│   ├── preload.js      # IPC bridge
│   ├── index.html      # UI
│   ├── styles.css      # AMOLED dark theme
│   ├── renderer.js     # Timer + storage + canvas ring + analytics
│   ├── manifest.json   # PWA manifest
│   ├── sw.js           # Service worker
│   └── icons/          # App icon
├── package.json
├── start.bat
└── README.md
```

## License

MIT
