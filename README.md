# DeepFocus

A lightweight, always-on study time tracker. Under 5MB. Pure black AMOLED display.

Built with [Tauri](https://tauri.app) — uses your system's webview instead of bundling a browser.

## Features

- **Precise Timer** — Start, pause, resume with second-level counting
- **Lightweight** — Under 5MB installer (vs 150MB+ for Electron apps)
- **Always-on AMOLED Display** — Pure black theme, minimal power
- **Crash Recovery** — Auto-recovers after shutdown (up to 30 min)
- **Auto-Start** — Launches silently on boot
- **System Tray** — Minimize to tray, always accessible
- **Circular Progress Ring** — Visual daily goal tracker
- **Daily Goal** — Customizable (default 6 hours)
- **Analytics** — Weekly chart, streak counter, session history
- **Break Reminders** — Configurable rest alerts
- **Cross-Platform** — Windows (Tauri) + Android (PWA)
- **Always on Top** — Lockscreen-style widget

## Download

- **Windows:** [Releases page](https://github.com/owaissh59-spec/DeepFocus/releases)
- **Android:** Open https://owaissh59-spec.github.io/DeepFocus/ in Chrome → "Add to Home Screen"

## Build from Source

Requires: [Rust](https://rustup.rs), [Node.js](https://nodejs.org)

```bash
npm install
npx tauri build
```

Output in `src-tauri/target/release/bundle/`

## Project Structure

```
DeepFocus/
├── src/                    # Frontend (HTML/CSS/JS)
│   ├── index.html
│   ├── styles.css
│   ├── renderer.js
│   ├── manifest.json       # PWA
│   ├── sw.js               # Service worker
│   └── icons/
├── src-tauri/              # Tauri backend (Rust)
│   ├── Cargo.toml
│   ├── tauri.conf.json
│   └── src/main.rs
├── generate-icons.js
├── package.json
└── README.md
```

## License

MIT
