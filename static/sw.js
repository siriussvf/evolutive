const CACHE_NAME = 'ie-cache-v1';
const ASSETS = [
    '/chat',
    '/static/css/chat_style.css',
    '/static/android-chrome-192.png',
    '/static/apple-touch-icon.png'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            // We don't force cache everything yet as it's a dynamic app
            return cache.addAll(ASSETS);
        })
    );
});

self.addEventListener('fetch', (event) => {
    // Simple network-first or pass-through for now to avoid breaking the chat streaming
    event.respondWith(
        fetch(event.request).catch(() => {
            return caches.match(event.request);
        })
    );
});
