
var our_cache = 'toasauti-cache';

var filesToCache = [
  '/',
  '../static/css/*',
  '../static/js/*',
  '../static/img/*'
];

self.addEventListener('install', function(event) {
	event.waitUntil(caches.open(our_cache).then(function(cache) {
        return cache.addAll(filesToCache);
      })
  );

	console.log("I am installed..!");
});

self.addEventListener('fetch', function(event) {
  event.respondWith(caches.match(event.request).then(function(response) {
        if (response) {
          return response;
        }
        return fetch(event.request);
      }
    )
  );
});