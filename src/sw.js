/**
 * DeepFocus - Service Worker
 * Network-first with a version-stamped cache so app updates are picked up
 * immediately (no more stale "old features" after an update), while still
 * working offline.
 *
 * The cache version comes from the registration URL query (?v=<appVersion>),
 * so every release gets a fresh cache and old caches are purged on activate.
 * IMPORTANT: this only touches the Cache Storage API - it never touches
 * IndexedDB or localStorage, so study history and settings are preserved.
 */

const VERSION = new URL(self.location).searchParams.get('v') || 'dev';
const CACHE_NAME = 'deepfocus-' + VERSION;

const ASSETS_TO_CACHE = [
    './',
    './index.html',
    './styles.css',
    './renderer.js',
    './window-controls.js',
    './manifest.json'
];

// Install - pre-cache the shell for this version, then take over ASAP.
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(ASSETS_TO_CACHE).catch(() => {}))
            .then(() => self.skipWaiting())
    );
});

// Activate - delete every cache that isn't the current version, then claim.
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys()
            .then(keys => Promise.all(
                keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
            ))
            .then(() => self.clients.claim())
    );
});

// Fetch - network-first so the freshest assets win; fall back to cache offline.
self.addEventListener('fetch', (event) => {
    const req = event.request;
    if (req.method !== 'GET') return;

    event.respondWith(
        fetch(req)
            .then(networkResponse => {
                if (networkResponse && networkResponse.status === 200) {
                    const clone = networkResponse.clone();
                    caches.open(CACHE_NAME).then(cache => cache.put(req, clone)).catch(() => {});
                }
                return networkResponse;
            })
            .catch(() => caches.match(req).then(cached => {
                if (cached) return cached;
                if (req.destination === 'document') return caches.match('./index.html');
                return Response.error();
            }))
    );
});

// Keep alive for timer accuracy
self.addEventListener('message', (event) => {
    if (event.data === 'keepalive' && event.source) {
        event.source.postMessage('alive');
    }
});
