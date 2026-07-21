/**
 * Study Tracker - Renderer Process
 * Timer logic, Canvas ring, data persistence, analytics
 */

// ============================================
// DATA STORAGE LAYER
// ============================================

class StudyStorage {
    constructor() {
        this.DB_NAME = 'StudyTrackerDB';
        this.DB_VERSION = 1;
        this.db = null;
        this.fallbackToLocalStorage = false;
    }

    async init() {
        try {
            this.db = await this.openDB();
        } catch (e) {
            console.warn('IndexedDB unavailable, using localStorage', e);
            this.fallbackToLocalStorage = true;
        }
    }

    openDB() {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open(this.DB_NAME, this.DB_VERSION);
            request.onerror = () => reject(request.error);
            request.onsuccess = () => resolve(request.result);
            request.onupgradeneeded = (event) => {
                const db = event.target.result;
                if (!db.objectStoreNames.contains('days')) {
                    const store = db.createObjectStore('days', { keyPath: 'date' });
                    store.createIndex('date', 'date', { unique: true });
                }
            };
        });
    }

    getTodayKey() {
        return new Date().toISOString().split('T')[0];
    }

    async saveDay(dayData) {
        if (this.fallbackToLocalStorage) {
            const all = this.getAllDaysFromLS();
            all[dayData.date] = dayData;
            localStorage.setItem('studytracker_days', JSON.stringify(all));
            return;
        }
        return new Promise((resolve, reject) => {
            const tx = this.db.transaction('days', 'readwrite');
            tx.objectStore('days').put(dayData).onsuccess = () => resolve();
            tx.onerror = () => reject(tx.error);
        });
    }

    async getDay(dateKey) {
        if (this.fallbackToLocalStorage) {
            return this.getAllDaysFromLS()[dateKey] || null;
        }
        return new Promise((resolve, reject) => {
            const tx = this.db.transaction('days', 'readonly');
            const req = tx.objectStore('days').get(dateKey);
            req.onsuccess = () => resolve(req.result || null);
            req.onerror = () => reject(req.error);
        });
    }

    async getAllDays() {
        if (this.fallbackToLocalStorage) {
            return Object.values(this.getAllDaysFromLS()).sort((a, b) => b.date.localeCompare(a.date));
        }
        return new Promise((resolve, reject) => {
            const tx = this.db.transaction('days', 'readonly');
            const req = tx.objectStore('days').getAll();
            req.onsuccess = () => resolve((req.result || []).sort((a, b) => b.date.localeCompare(a.date)));
            req.onerror = () => reject(req.error);
        });
    }

    getAllDaysFromLS() {
        try { return JSON.parse(localStorage.getItem('studytracker_days') || '{}'); }
        catch { return {}; }
    }

    saveState(state) { localStorage.setItem('studytracker_state', JSON.stringify(state)); }
    loadState() { try { return JSON.parse(localStorage.getItem('studytracker_state')); } catch { return null; } }
    clearState() { localStorage.removeItem('studytracker_state'); }

    async saveSetting(key, value) { localStorage.setItem(`st_${key}`, JSON.stringify(value)); }
    async getSetting(key, defaultValue) {
        try { const v = localStorage.getItem(`st_${key}`); return v !== null ? JSON.parse(v) : defaultValue; }
        catch { return defaultValue; }
    }
}

// ============================================
// TIMER ENGINE
// ============================================

class StudyTimer {
    constructor(storage) {
        this.storage = storage;
        this.state = 'stopped';
        this.elapsedMs = 0;
        this.totalTodayMs = 0;
        this.sessionStartTime = null;
        this.sessions = [];
        this.intervalId = null;
        this.breakReminderTimeout = null;
        this.breakReminderMinutes = 45;
    }

    async init() {
        this.breakReminderMinutes = await this.storage.getSetting('breakReminder', 45);
        const savedState = this.storage.loadState();

        if (savedState && savedState.date === this.storage.getTodayKey()) {
            this.sessions = savedState.sessions || [];
            this.totalTodayMs = savedState.totalTodayMs || 0;
            this.elapsedMs = savedState.currentElapsed || 0;

            if (savedState.state === 'running' && savedState.lastTick) {
                const missedMs = Date.now() - savedState.lastTick;
                if (missedMs < 30 * 60 * 1000) {
                    this.elapsedMs += missedMs;
                    this.totalTodayMs += missedMs;
                    this.state = 'running';
                    this.sessionStartTime = Date.now();
                    this.startTicking();
                } else {
                    this.sessions.push({ start: savedState.sessionStartTime, end: savedState.lastTick, duration: savedState.currentElapsed });
                    this.elapsedMs = 0;
                    this.state = 'paused';
                }
            } else if (savedState.state === 'paused') {
                this.state = 'paused';
            }
        } else if (savedState && savedState.date !== this.storage.getTodayKey()) {
            await this.finalizePreviousDay(savedState);
        }
    }

    async finalizePreviousDay(savedState) {
        if (savedState && savedState.sessions && savedState.sessions.length > 0) {
            await this.storage.saveDay({
                date: savedState.date,
                totalMs: savedState.totalTodayMs || 0,
                sessions: savedState.sessions,
                sessionCount: savedState.sessions.length
            });
        }
        this.storage.clearState();
        this.sessions = [];
        this.totalTodayMs = 0;
        this.elapsedMs = 0;
    }

    start() {
        if (this.state === 'running') return;
        this.state = 'running';
        this.sessionStartTime = Date.now();
        this.elapsedMs = 0;
        this.startTicking();
        this.startBreakReminder();
        this.persistState();
    }

    pause() {
        if (this.state !== 'running') return;
        this.state = 'paused';
        this.stopTicking();
        this.clearBreakReminder();
        this.sessions.push({ start: this.sessionStartTime, end: Date.now(), duration: this.elapsedMs });
        this.totalTodayMs += this.elapsedMs;
        this.persistState();
    }

    resume() {
        if (this.state !== 'paused') return;
        this.state = 'running';
        this.sessionStartTime = Date.now();
        this.elapsedMs = 0;
        this.startTicking();
        this.startBreakReminder();
        this.persistState();
    }

    async endDay() {
        if (this.state === 'running') this.pause();
        await this.storage.saveDay({
            date: this.storage.getTodayKey(),
            totalMs: this.totalTodayMs,
            sessions: this.sessions,
            sessionCount: this.sessions.length
        });
        this.state = 'stopped';
        this.elapsedMs = 0;
        this.totalTodayMs = 0;
        this.sessions = [];
        this.storage.clearState();
        this.stopTicking();
        this.clearBreakReminder();
    }

    startTicking() {
        this.stopTicking();
        this.intervalId = setInterval(() => {
            if (this.state === 'running') {
                this.elapsedMs = Date.now() - this.sessionStartTime;
                this.persistState();
            }
        }, 1000);
    }

    stopTicking() { if (this.intervalId) { clearInterval(this.intervalId); this.intervalId = null; } }

    startBreakReminder() {
        this.clearBreakReminder();
        if (this.breakReminderMinutes > 0) {
            this.breakReminderTimeout = setTimeout(() => this.onBreakReminder(), this.breakReminderMinutes * 60 * 1000);
        }
    }

    clearBreakReminder() { if (this.breakReminderTimeout) { clearTimeout(this.breakReminderTimeout); this.breakReminderTimeout = null; } }

    onBreakReminder() {
        showBreakNotification();
        if ('Notification' in window && Notification.permission === 'granted') {
            new Notification('Study Tracker', { body: `${this.breakReminderMinutes} min passed. Take a break!` });
        }
        this.startBreakReminder();
    }

    persistState() {
        this.storage.saveState({
            state: this.state, date: this.storage.getTodayKey(),
            sessions: this.sessions, totalTodayMs: this.totalTodayMs,
            currentElapsed: this.elapsedMs, sessionStartTime: this.sessionStartTime, lastTick: Date.now()
        });
    }

    getCurrentElapsed() { return this.state === 'running' ? Date.now() - this.sessionStartTime : this.elapsedMs; }
    getTotalToday() { return this.state === 'running' ? this.totalTodayMs + (Date.now() - this.sessionStartTime) : this.totalTodayMs; }
    getSessionCount() { return this.sessions.length + (this.state === 'running' ? 1 : 0); }
}

// ============================================
// CANVAS RING RENDERER
// ============================================

class RingRenderer {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.progress = 0; // 0 to 1
        this.isRunning = false;
        this.resize();
        window.addEventListener('resize', () => this.resize());
    }

    resize() {
        // Fill available space in .timer-ring-wrapper
        const wrapper = this.canvas.parentElement;
        const available = Math.min(wrapper.clientWidth, wrapper.clientHeight);
        // Use as much space as possible - at least 85% of available
        const size = Math.max(200, Math.floor(available * 0.92));
        const dpr = window.devicePixelRatio || 1;
        this.canvas.width = size * dpr;
        this.canvas.height = size * dpr;
        this.canvas.style.width = size + 'px';
        this.canvas.style.height = size + 'px';
        this.ctx.scale(dpr, dpr);
        this.size = size;
        this.draw();
    }

    draw() {
        const ctx = this.ctx;
        const size = this.size;
        const cx = size / 2;
        const cy = size / 2;
        const radius = (size / 2) - 14; // leave padding for stroke
        const lineWidth = 5;

        ctx.clearRect(0, 0, size, size);

        // Background ring
        ctx.beginPath();
        ctx.arc(cx, cy, radius, 0, Math.PI * 2);
        ctx.strokeStyle = '#151515';
        ctx.lineWidth = lineWidth;
        ctx.stroke();

        // Progress ring
        if (this.progress > 0) {
            const startAngle = -Math.PI / 2;
            const endAngle = startAngle + (Math.PI * 2 * Math.min(this.progress, 1));

            // Create gradient
            const gradient = ctx.createLinearGradient(0, 0, size, size);
            gradient.addColorStop(0, '#448aff');
            gradient.addColorStop(1, '#00e676');

            ctx.beginPath();
            ctx.arc(cx, cy, radius, startAngle, endAngle);
            ctx.strokeStyle = gradient;
            ctx.lineWidth = lineWidth;
            ctx.lineCap = 'round';
            ctx.stroke();

            // Glow effect when running
            if (this.isRunning) {
                ctx.beginPath();
                ctx.arc(cx, cy, radius, startAngle, endAngle);
                ctx.strokeStyle = 'rgba(0, 230, 118, 0.15)';
                ctx.lineWidth = lineWidth + 8;
                ctx.lineCap = 'round';
                ctx.stroke();
            }
        }

        // Subtle tick marks every hour (if goal > 0)
        if (this.goalHours && this.goalHours > 0) {
            ctx.save();
            for (let i = 0; i < this.goalHours; i++) {
                const angle = -Math.PI / 2 + (Math.PI * 2 * i / this.goalHours);
                const x1 = cx + Math.cos(angle) * (radius - 8);
                const y1 = cy + Math.sin(angle) * (radius - 8);
                const x2 = cx + Math.cos(angle) * (radius + 2);
                const y2 = cy + Math.sin(angle) * (radius + 2);
                ctx.beginPath();
                ctx.moveTo(x1, y1);
                ctx.lineTo(x2, y2);
                ctx.strokeStyle = '#222';
                ctx.lineWidth = 1;
                ctx.lineCap = 'round';
                ctx.stroke();
            }
            ctx.restore();
        }
    }

    update(progress, isRunning, goalHours) {
        this.progress = progress;
        this.isRunning = isRunning;
        this.goalHours = goalHours;
        this.draw();
    }
}

// ============================================
// UI CONTROLLER
// ============================================

class UIController {
    constructor(timer, storage) {
        this.timer = timer;
        this.storage = storage;
        this.dailyGoalHours = 6;
        this.dimTimeout = null;
        this.isDimmed = false;
        this.ring = null;
        // Always-On Display state
        this.aodActive = false;
        this.aodInterval = null;
        this.aodDriftInterval = null;
    }

    async init() {
        this.dailyGoalHours = await this.storage.getSetting('dailyGoal', 6);
        this.ring = new RingRenderer(document.getElementById('timer-canvas'));
        this.bindEvents();
        this.startClock();
        this.updateUI();
        this.startUIRefresh();
        this.setupDimming();
        this.requestNotificationPermission();
        this.loadSettingsToUI();
    }

    bindEvents() {
        // Timer controls
        document.getElementById('btn-start').addEventListener('click', () => this.onStart());
        document.getElementById('btn-pause').addEventListener('click', () => this.onPause());
        document.getElementById('btn-resume').addEventListener('click', () => this.onResume());
        document.getElementById('btn-stop').addEventListener('click', () => this.onEndDay());

        // Menu navigation
        document.getElementById('btn-menu').addEventListener('click', () => this.showMenu());
        document.getElementById('btn-back').addEventListener('click', () => this.showMain());

        // Settings - auto save on change
        document.getElementById('daily-goal-input').addEventListener('change', () => this.saveAllSettings());
        document.getElementById('always-on-top-toggle').addEventListener('change', () => this.saveAllSettings());
        document.getElementById('auto-start-toggle').addEventListener('change', () => this.saveAllSettings());
        document.getElementById('break-reminder-input').addEventListener('change', () => this.saveAllSettings());
        document.getElementById('aod-toggle').addEventListener('change', () => this.saveAllSettings());

        // Tap the always-on view to leave it
        const aodOverlay = document.getElementById('aod-overlay');
        if (aodOverlay) aodOverlay.addEventListener('click', () => this.exitAOD());

        // Dimming
        document.addEventListener('click', () => this.wakeFromDim());
        document.addEventListener('keydown', () => this.wakeFromDim());
        document.addEventListener('mousemove', () => this.wakeFromDim());

        // Visibility
        document.addEventListener('visibilitychange', () => { if (!document.hidden) this.updateUI(); });
        window.addEventListener('beforeunload', () => this.timer.persistState());
        window.addEventListener('resize', () => { if (this.ring) this.ring.resize(); });
    }

    async loadSettingsToUI() {
        document.getElementById('daily-goal-input').value = this.dailyGoalHours;
        document.getElementById('break-reminder-input').value = this.timer.breakReminderMinutes;
        document.getElementById('always-on-top-toggle').checked = await this.storage.getSetting('alwaysOnTop', true);
        document.getElementById('auto-start-toggle').checked = await this.storage.getSetting('autoStart', true);
        const aodOn = await this.storage.getSetting('aodEnabled', false);
        document.getElementById('aod-toggle').checked = aodOn;
        // Keep the native layer in sync with the stored preference
        try { window.Android && window.Android.setAodEnabled(!!aodOn); } catch (e) {}
    }

    onStart() { this.timer.start(); this.updateUI(); }
    onPause() { this.timer.pause(); this.updateUI(); }
    onResume() { this.timer.resume(); this.updateUI(); }

    async onEndDay() {
        if (this.timer.sessions.length === 0 && this.timer.state === 'stopped') return;
        if (confirm('End today\'s study session? This will save your progress.')) {
            await this.timer.endDay();
            this.updateUI();
        }
    }

    // Clock
    startClock() {
        this.updateClock();
        setInterval(() => this.updateClock(), 1000);
    }

    updateClock() {
        const now = new Date();
        document.getElementById('current-time').textContent = now.toLocaleTimeString('en-US', {
            hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: true
        });
        document.getElementById('current-date').textContent = now.toLocaleDateString('en-US', {
            weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
        });

        // Day change check
        const today = this.storage.getTodayKey();
        const stateDate = this.storage.loadState()?.date;
        if (stateDate && stateDate !== today) {
            this.timer.finalizePreviousDay(this.storage.loadState());
            this.updateUI();
        }
    }

    startUIRefresh() {
        setInterval(() => {
            if (this.aodActive) return; // AOD view handles its own minimal updates
            if (this.timer.state === 'running') {
                this.updateTimerDisplay();
                this.updateRing();
            }
        }, 1000);
    }

    updateTimerDisplay() {
        const elapsed = this.timer.getCurrentElapsed();
        document.getElementById('study-timer').textContent = this.formatTime(elapsed);
        document.getElementById('total-today').textContent = `${this.formatTimeShort(this.timer.getTotalToday())} today`;
        document.getElementById('session-count').textContent = `${this.timer.getSessionCount()} sessions`;
    }

    updateRing() {
        const totalToday = this.timer.getTotalToday();
        const goalMs = this.dailyGoalHours * 60 * 60 * 1000;
        const percent = Math.min(1, totalToday / goalMs);

        // Progress bar
        document.getElementById('progress-fill').style.width = `${Math.round(percent * 100)}%`;
        document.getElementById('progress-percent').textContent = `${Math.round(percent * 100)}%`;
        document.getElementById('goal-hours').textContent = this.dailyGoalHours;

        // Canvas ring
        if (this.ring) {
            this.ring.update(percent, this.timer.state === 'running', this.dailyGoalHours);
        }
    }

    updateUI() {
        const state = this.timer.state;

        // Buttons
        document.getElementById('btn-start').classList.toggle('hidden', state !== 'stopped');
        document.getElementById('btn-pause').classList.toggle('hidden', state !== 'running');
        document.getElementById('btn-resume').classList.toggle('hidden', state !== 'paused');
        document.getElementById('btn-stop').classList.toggle('hidden', state === 'stopped');

        // Status
        document.getElementById('timer-status-dot').className = 'status-dot ' + state;
        const labels = { stopped: 'Ready', running: 'Focused', paused: 'Break' };
        document.getElementById('timer-status-text').textContent = labels[state];

        // Body class for glow
        document.body.classList.toggle('timer-running', state === 'running');

        this.updateTimerDisplay();
        this.updateRing();
    }

    // ============================================
    // MENU SCREEN
    // ============================================

    async showMenu() {
        document.getElementById('main-screen').classList.remove('active');
        document.getElementById('menu-screen').classList.add('active');
        await this.loadSettingsToUI();
        await this.renderHistory();
    }

    showMain() {
        document.getElementById('menu-screen').classList.remove('active');
        document.getElementById('main-screen').classList.add('active');
        // Refresh ring size since it may have been hidden
        setTimeout(() => { if (this.ring) this.ring.resize(); }, 50);
    }

    async saveAllSettings() {
        const goal = parseInt(document.getElementById('daily-goal-input').value) || 6;
        const breakReminder = parseInt(document.getElementById('break-reminder-input').value) || 0;
        const alwaysOnTop = document.getElementById('always-on-top-toggle').checked;
        const autoStart = document.getElementById('auto-start-toggle').checked;
        const aodEnabled = document.getElementById('aod-toggle').checked;

        this.dailyGoalHours = goal;
        this.timer.breakReminderMinutes = breakReminder;

        await this.storage.saveSetting('dailyGoal', goal);
        await this.storage.saveSetting('breakReminder', breakReminder);
        await this.storage.saveSetting('alwaysOnTop', alwaysOnTop);
        await this.storage.saveSetting('autoStart', autoStart);
        await this.storage.saveSetting('aodEnabled', aodEnabled);

        // Tell the Android layer whether to wake the screen into the AOD view
        try { window.Android && window.Android.setAodEnabled(!!aodEnabled); } catch (e) {}

        if (window.__TAURI__) {
            // Tauri handles these via plugin config
        }

        this.updateRing();
    }

    // ============================================
    // HISTORY & ANALYTICS
    // ============================================

    async renderHistory() {
        const allDays = await this.storage.getAllDays();
        const todayKey = this.storage.getTodayKey();
        let daysWithToday = [...allDays];

        if (this.timer.getTotalToday() > 0) {
            const todayData = { date: todayKey, totalMs: this.timer.getTotalToday(), sessions: this.timer.sessions, sessionCount: this.timer.getSessionCount() };
            const idx = daysWithToday.findIndex(d => d.date === todayKey);
            if (idx >= 0) daysWithToday[idx] = todayData;
            else daysWithToday.unshift(todayData);
        }

        this.renderStats(daysWithToday);
        this.renderWeeklyChart(daysWithToday);
        this.renderHistoryList(daysWithToday);
    }

    renderStats(days) {
        const now = new Date();
        const weekStart = new Date(now);
        weekStart.setDate(now.getDate() - now.getDay());
        weekStart.setHours(0, 0, 0, 0);
        const weekStartKey = weekStart.toISOString().split('T')[0];

        const weekDays = days.filter(d => d.date >= weekStartKey);
        const weekTotalMs = weekDays.reduce((sum, d) => sum + (d.totalMs || 0), 0);
        document.getElementById('stat-week-total').textContent = this.formatTimeShort(weekTotalMs);

        const recentDays = days.slice(0, 7);
        const avgMs = recentDays.length > 0 ? recentDays.reduce((sum, d) => sum + (d.totalMs || 0), 0) / recentDays.length : 0;
        document.getElementById('stat-avg').textContent = this.formatTimeShort(avgMs);

        document.getElementById('stat-streak').textContent = this.calculateStreak(days);
    }

    calculateStreak(days) {
        let streak = 0;
        const today = new Date(); today.setHours(0, 0, 0, 0);
        for (let i = 0; i < 365; i++) {
            const d = new Date(today); d.setDate(today.getDate() - i);
            const key = d.toISOString().split('T')[0];
            const found = days.find(x => x.date === key);
            if (found && found.totalMs > 0) streak++;
            else if (i === 0) continue;
            else break;
        }
        return streak;
    }

    renderWeeklyChart(days) {
        const chart = document.getElementById('weekly-chart');
        chart.innerHTML = '';
        const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        const today = new Date();
        const weekData = [];

        for (let i = 6; i >= 0; i--) {
            const date = new Date(today); date.setDate(today.getDate() - i);
            const key = date.toISOString().split('T')[0];
            const d = days.find(x => x.date === key);
            weekData.push({ day: dayNames[date.getDay()], ms: d ? d.totalMs : 0, isToday: i === 0 });
        }

        const maxMs = Math.max(...weekData.map(d => d.ms), 1);
        weekData.forEach(data => {
            const item = document.createElement('div');
            item.className = 'bar-item';
            const pct = (data.ms / maxMs) * 100;
            const hrs = (data.ms / 3600000).toFixed(1);
            item.innerHTML = `
                <div class="bar-value">${hrs}h</div>
                <div class="bar" style="height:${Math.max(pct, 2)}%${data.isToday ? ';background:linear-gradient(to top,#00e676,#69f0ae)' : ''}"></div>
                <div class="bar-label" style="${data.isToday ? 'color:#00e676' : ''}">${data.day}</div>`;
            chart.appendChild(item);
        });
    }

    renderHistoryList(days) {
        const container = document.getElementById('history-entries');
        container.innerHTML = '';
        if (days.length === 0) {
            container.innerHTML = '<p style="color:#333;text-align:center;padding:20px">No sessions yet</p>';
            return;
        }
        days.slice(0, 30).forEach(day => {
            const date = new Date(day.date + 'T00:00:00');
            const el = document.createElement('div');
            el.className = 'history-entry';
            el.innerHTML = `<div><div class="history-entry-date">${date.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}</div><div class="history-entry-day">${date.toLocaleDateString('en-US', { weekday: 'long' })}</div></div><div style="text-align:right"><div class="history-entry-time">${this.formatTimeShort(day.totalMs)}</div><div class="history-entry-sessions">${day.sessionCount || 0} session${(day.sessionCount || 0) !== 1 ? 's' : ''}</div></div>`;
            container.appendChild(el);
        });
    }

    // ============================================
    // DIMMING & WAKE LOCK
    // ============================================

    setupDimming() { this.resetDimTimer(); }

    resetDimTimer() {
        if (this.dimTimeout) clearTimeout(this.dimTimeout);
        this.dimTimeout = setTimeout(() => {
            if (this.timer.state !== 'stopped') { document.body.classList.add('dimmed'); this.isDimmed = true; }
        }, 60000);
    }

    wakeFromDim() {
        if (this.isDimmed) { document.body.classList.remove('dimmed'); this.isDimmed = false; }
        this.resetDimTimer();
    }

    async requestWakeLock() {
        if ('wakeLock' in navigator) {
            try {
                this.wakeLock = await navigator.wakeLock.request('screen');
                this.wakeLock.addEventListener('release', () => {
                    document.addEventListener('visibilitychange', async () => {
                        if (!document.hidden && this.timer.state === 'running') this.wakeLock = await navigator.wakeLock.request('screen');
                    }, { once: true });
                });
            } catch (e) { /* unsupported */ }
        }
    }

    releaseWakeLock() { if (this.wakeLock) { this.wakeLock.release(); this.wakeLock = null; } }

    // ============================================
    // ALWAYS-ON DISPLAY (AOD)
    // Called by the native layer via window.enterAOD / window.exitAOD
    // when the screen turns off/on. Keeps only a few dim pixels lit.
    // ============================================

    enterAOD() {
        if (this.aodActive) return;
        this.aodActive = true;
        document.body.classList.add('aod-active');
        const overlay = document.getElementById('aod-overlay');
        if (overlay) overlay.classList.add('active');

        this.updateAOD();
        // Timer counts seconds, so refresh once per second - just a text swap.
        this.aodInterval = setInterval(() => this.updateAOD(), 1000);
        // Shift the pixels every 60s to avoid AMOLED burn-in.
        this.driftAOD();
        this.aodDriftInterval = setInterval(() => this.driftAOD(), 60000);
    }

    exitAOD() {
        if (!this.aodActive) return;
        this.aodActive = false;
        document.body.classList.remove('aod-active');
        const overlay = document.getElementById('aod-overlay');
        if (overlay) overlay.classList.remove('active');

        if (this.aodInterval) { clearInterval(this.aodInterval); this.aodInterval = null; }
        if (this.aodDriftInterval) { clearInterval(this.aodDriftInterval); this.aodDriftInterval = null; }

        // Restore normal brightness / release the native wake lock.
        try {
            if (window.Android && window.Android.onAodDismissed) window.Android.onAodDismissed();
            else if (window.Android && window.Android.setBrightness) window.Android.setBrightness(-1);
        } catch (e) {}
        this.updateUI();
    }

    updateAOD() {
        const now = new Date();
        const clock = document.getElementById('aod-clock');
        const t = document.getElementById('aod-timer');
        const label = document.getElementById('aod-label');
        if (clock) clock.textContent = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: true });
        if (t) t.textContent = this.formatTime(this.timer.getCurrentElapsed());
        if (label) {
            const map = { running: 'FOCUS', paused: 'BREAK', stopped: 'READY' };
            label.textContent = map[this.timer.state] || 'FOCUS';
        }
    }

    driftAOD() {
        const inner = document.getElementById('aod-inner');
        if (!inner) return;
        const dx = Math.round((Math.random() - 0.5) * 40); // +/-20px
        const dy = Math.round((Math.random() - 0.5) * 40);
        inner.style.transform = `translate(${dx}px, ${dy}px)`;
    }

    requestNotificationPermission() {
        if ('Notification' in window && Notification.permission === 'default') Notification.requestPermission();
    }

    // ============================================
    // UTILITIES
    // ============================================

    formatTime(ms) {
        const s = Math.floor(ms / 1000);
        return `${String(Math.floor(s / 3600)).padStart(2, '0')}:${String(Math.floor((s % 3600) / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;
    }

    formatTimeShort(ms) {
        const m = Math.floor(ms / 60000);
        const h = Math.floor(m / 60);
        return h > 0 ? `${h}h ${m % 60}m` : `${m}m`;
    }
}

// ============================================
// HELPERS
// ============================================

function showBreakNotification() {
    const n = document.createElement('div');
    n.className = 'break-notification';
    n.textContent = 'Time for a break! Stretch and rest your eyes.';
    document.body.appendChild(n);
    setTimeout(() => n.remove(), 8000);
    n.addEventListener('click', () => n.remove());
}

// ============================================
// INIT
// ============================================

async function initApp() {
    const storage = new StudyStorage();
    await storage.init();

    const timer = new StudyTimer(storage);
    await timer.init();

    const ui = new UIController(timer, storage);
    await ui.init();

    registerServiceWorker();

    // Hook Electron notifications
    const origStart = timer.start.bind(timer);
    const origPause = timer.pause.bind(timer);
    const origResume = timer.resume.bind(timer);
    const origEnd = timer.endDay.bind(timer);

    timer.start = () => { origStart(); notifyElectron('running'); ui.requestWakeLock(); };
    timer.pause = () => { origPause(); notifyElectron('paused'); ui.releaseWakeLock(); };
    timer.resume = () => { origResume(); notifyElectron('running'); ui.requestWakeLock(); };
    timer.endDay = async () => { await origEnd(); notifyElectron('stopped'); ui.releaseWakeLock(); };

    if (timer.state === 'running') { notifyElectron('running'); ui.requestWakeLock(); }

    window.studyApp = { timer, storage, ui };

    // Expose Always-On Display hooks for the native (Android) layer to call
    // when the power button turns the screen off / back on.
    window.enterAOD = () => ui.enterAOD();
    window.exitAOD = () => ui.exitAOD();
}

function notifyElectron(state) {
    // Report study-session state to the native layer so it only wakes the
    // screen into the always-on view while a session is actually running.
    try { window.Android && window.Android.setTimerRunning(state === 'running'); } catch (e) {}
}

function registerServiceWorker() {
    if ('serviceWorker' in navigator && !window.__TAURI__) {
        navigator.serviceWorker.register('sw.js').then(reg => {
            setInterval(() => { if (window.studyApp?.timer.state === 'running') reg.active?.postMessage('keepalive'); }, 20000);
        }).catch(() => {});
    }
}

initApp().catch(console.error);
