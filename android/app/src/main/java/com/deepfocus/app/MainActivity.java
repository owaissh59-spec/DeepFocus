package com.deepfocus.app;

import android.app.KeyguardManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.os.Build;
import android.os.Bundle;
import android.os.PowerManager;
import android.view.View;
import android.view.WindowManager;
import android.webkit.JavascriptInterface;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebSettings;
import android.webkit.WebChromeClient;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private WebView webView;
    private PowerManager.WakeLock cpuWakeLock;   // keeps the timer ticking (CPU only)
    private PowerManager.WakeLock aodWakeLock;    // turns the screen back on for the AOD view

    private SharedPreferences prefs;
    private BroadcastReceiver screenReceiver;

    // Live state pushed from the web UI via the JS bridge
    private volatile boolean aodEnabled = false;
    private volatile boolean timerRunning = false;

    // Tracks the always-on view lifecycle so we don't fight our own wake events.
    private volatile boolean aodShowing = false;   // dim view currently up
    private volatile boolean selfWake = false;      // the next SCREEN_ON is one we caused

    // Brightness level used while the always-on view is showing (0.0 - 1.0).
    // Default is kept low to minimise power draw on an AMOLED panel; the user
    // can raise it from the settings screen (e.g. for daylight visibility).
    private static final float DEFAULT_AOD_BRIGHTNESS = 0.06f;
    private volatile float aodBrightness = DEFAULT_AOD_BRIGHTNESS;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        prefs = getSharedPreferences("deepfocus", Context.MODE_PRIVATE);
        aodEnabled = prefs.getBoolean("aod_enabled", false);
        aodBrightness = prefs.getFloat("aod_brightness", DEFAULT_AOD_BRIGHTNESS);

        // === LOCKSCREEN VISIBILITY ===
        // Show this activity on top of the lock screen
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O_MR1) {
            setShowWhenLocked(true);
            setTurnScreenOn(true);
            KeyguardManager km = (KeyguardManager) getSystemService(Context.KEYGUARD_SERVICE);
            if (km != null) {
                km.requestDismissKeyguard(this, null);
            }
        } else {
            getWindow().addFlags(
                WindowManager.LayoutParams.FLAG_SHOW_WHEN_LOCKED |
                WindowManager.LayoutParams.FLAG_TURN_SCREEN_ON |
                WindowManager.LayoutParams.FLAG_DISMISS_KEYGUARD
            );
        }

        // Keep screen on (like always-on display)
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

        // Fullscreen immersive - acts like lockscreen wallpaper
        getWindow().getDecorView().setSystemUiVisibility(
            View.SYSTEM_UI_FLAG_LAYOUT_STABLE |
            View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION |
            View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN |
            View.SYSTEM_UI_FLAG_HIDE_NAVIGATION |
            View.SYSTEM_UI_FLAG_FULLSCREEN |
            View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
        );

        // Black status/nav bars
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            getWindow().setStatusBarColor(0xFF000000);
            getWindow().setNavigationBarColor(0xFF000000);
        }

        // Setup WebView
        webView = new WebView(this);
        setContentView(webView);

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setCacheMode(WebSettings.LOAD_DEFAULT);
        settings.setAllowFileAccess(true);

        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());
        webView.setBackgroundColor(0xFF000000);

        // Expose the native bridge to JavaScript (window.Android.*)
        webView.addJavascriptInterface(new AndroidBridge(), "Android");

        // Load the app from assets
        webView.loadUrl("file:///android_asset/www/index.html");

        // === WAKE LOCK - keep CPU alive for timer ===
        PowerManager pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
        cpuWakeLock = pm.newWakeLock(
            PowerManager.PARTIAL_WAKE_LOCK,
            "DeepFocus::TimerLock"
        );
        cpuWakeLock.acquire();

        // Screen-dim wake lock used only to bring the display back for the AOD view.
        // Deprecated flags, but they remain the only mechanism for a normal app to
        // wake the screen into a dimmed always-on state.
        aodWakeLock = pm.newWakeLock(
            PowerManager.SCREEN_DIM_WAKE_LOCK | PowerManager.ACQUIRE_CAUSES_WAKEUP,
            "DeepFocus::AodLock"
        );

        // Listen for the power button turning the screen off/on.
        registerScreenReceiver();

        // Start foreground service to prevent kill
        Intent serviceIntent = new Intent(this, StudyTimerService.class);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            startForegroundService(serviceIntent);
        } else {
            startService(serviceIntent);
        }
    }

    // ============================================
    // SCREEN ON/OFF -> ALWAYS-ON DISPLAY
    // ============================================

    private void registerScreenReceiver() {
        screenReceiver = new BroadcastReceiver() {
            @Override
            public void onReceive(Context context, Intent intent) {
                String action = intent.getAction();
                if (Intent.ACTION_SCREEN_OFF.equals(action)) {
                    onScreenOff();
                } else if (Intent.ACTION_SCREEN_ON.equals(action)) {
                    onScreenOn();
                }
            }
        };
        IntentFilter filter = new IntentFilter();
        filter.addAction(Intent.ACTION_SCREEN_OFF);
        filter.addAction(Intent.ACTION_SCREEN_ON);
        registerReceiver(screenReceiver, filter);
    }

    // Power button pressed (or timeout) -> screen went off.
    // If enabled and a study session is active, re-show a dim always-on view.
    private void onScreenOff() {
        if (!aodEnabled || !timerRunning) {
            return;
        }
        // We're about to turn the screen back on ourselves; the resulting
        // ACTION_SCREEN_ON must NOT be treated as a user waking the device.
        selfWake = true;
        aodShowing = true;
        runOnUiThread(() -> {
            // Wake the display back on (dim) without unlocking the phone.
            if (aodWakeLock != null && !aodWakeLock.isHeld()) {
                // 12h safety cap; released on dismiss / destroy.
                aodWakeLock.acquire(12 * 60 * 60 * 1000L);
            }
            applyBrightness(aodBrightness);
            if (webView != null) {
                webView.evaluateJavascript("window.enterAOD && window.enterAOD();", null);
            }
        });
    }

    // Screen came on. If we caused it (to show AOD), keep the dim view.
    // Otherwise it was an external/user wake - nothing to do here; the user
    // dismisses the dim view by tapping it (-> onAodDismissed()).
    private void onScreenOn() {
        if (selfWake) {
            selfWake = false;
        }
    }

    private void applyBrightness(float level) {
        WindowManager.LayoutParams lp = getWindow().getAttributes();
        lp.screenBrightness = level; // -1f = follow system, 0..1 = manual
        getWindow().setAttributes(lp);
    }

    // ============================================
    // JS BRIDGE (window.Android.*)
    // ============================================

    private class AndroidBridge {
        @JavascriptInterface
        public void setAodEnabled(boolean enabled) {
            aodEnabled = enabled;
            prefs.edit().putBoolean("aod_enabled", enabled).apply();
        }

        @JavascriptInterface
        public boolean isAodEnabled() {
            return aodEnabled;
        }

        // The web UI reports whether a study session is currently running so we
        // only wake the screen for AOD while the user is actually studying.
        @JavascriptInterface
        public void setTimerRunning(boolean running) {
            timerRunning = running;
        }

        // Let the web UI dim/restore the panel (0..1, or -1 for system default).
        @JavascriptInterface
        public void setBrightness(final float level) {
            runOnUiThread(() -> applyBrightness(level));
        }

        // Persist the user's preferred always-on brightness (0..1). Applied the
        // next time the screen goes off during a session; if the dim view is
        // already showing, update the panel live.
        @JavascriptInterface
        public void setAodBrightness(final float level) {
            float v = level < 0f ? DEFAULT_AOD_BRIGHTNESS : Math.max(0.01f, Math.min(1f, level));
            aodBrightness = v;
            prefs.edit().putFloat("aod_brightness", v).apply();
            if (aodShowing) {
                runOnUiThread(() -> applyBrightness(aodBrightness));
            }
        }

        // The web UI calls this when the user taps the dim always-on view to
        // wake it fully: release the wake lock and restore system brightness.
        @JavascriptInterface
        public void onAodDismissed() {
            aodShowing = false;
            selfWake = false;
            runOnUiThread(() -> {
                if (aodWakeLock != null && aodWakeLock.isHeld()) {
                    aodWakeLock.release();
                }
                applyBrightness(-1f);
            });
        }
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        // Re-apply immersive mode whenever focus changes
        if (hasFocus) {
            getWindow().getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_LAYOUT_STABLE |
                View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION |
                View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN |
                View.SYSTEM_UI_FLAG_HIDE_NAVIGATION |
                View.SYSTEM_UI_FLAG_FULLSCREEN |
                View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
            );
        }
    }

    @Override
    protected void onDestroy() {
        if (screenReceiver != null) {
            try { unregisterReceiver(screenReceiver); } catch (Exception ignored) {}
            screenReceiver = null;
        }
        if (aodWakeLock != null && aodWakeLock.isHeld()) {
            aodWakeLock.release();
        }
        if (cpuWakeLock != null && cpuWakeLock.isHeld()) {
            cpuWakeLock.release();
        }
        super.onDestroy();
    }

    @Override
    public void onBackPressed() {
        // Don't close on back press - keep running like lockscreen
        if (webView.canGoBack()) {
            webView.goBack();
        }
    }
}
