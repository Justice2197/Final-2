var dataCacheName = 'mysite-cache';
var cacheName = 'mysite-pwa';
var filesToCache = [
    '/',
    "./../static",
    "./../static/img/adopcion.jpg",
    "./../static/img/crowfunding.jpg",
    "./../static/img/facebook.jpg",
    "./../static/img/googleplus.jpg",
    "./../static/img/instagram.jpg",
    "./../static/img/logo.png",
    "./../static/img/mail.jpg",
    "./../static/img/patita.png",
    "./../static/img/perro.jpeg",
    "./../static/img/perro.png",
    "./../static/img/perro1.jpg",
    "./../static/img/perro2.jpg",
    "./../static/img/perro3.jpeg",
    "./../static/img/perro4.jpg",
    "./../static/img/perro5.jpg",
    "./../static/img/perro6.jpg",
    "./../static/img/perro7.jpg",
    "./../static/img/perro8.jpg",
    "./../static/img/perro9.jpg",
    "./../static/img/perro10.JPG",
    "./../static/img/perro11.jpg",
    "./../static/img/perro12.jpg",
    "./../static/img/perro13.jpg",
    "./../static/img/perro20.jpg",
    "./../static/img/perro21.jpg",
    "./../static/img/rescate.jpg",
    "./../static/css/Estilo.css",
    "./../static/css/Estilo2.css",
    "./../static/materialize/css/matetialize.css",
    "./../static/materialize/css/materialize.min.css",
    "./../static/js/materialize.js",
    "./../static/js/materialize.min.js",
    "./../static/jquery-3.3.1.min.js"
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Cache open!');
        return cache.addAll(urlsToCache);
      })
  );
});


 self.addEventListener('activate', event => {
     // remove old caches
     event.waitUntil(
       caches.keys().then(keys => Promise.all(
         keys.map(key => {
           if (key != CACHE_NAME) {
             return caches.delete(key);
           }
         })
       )).then(() => {
         console.log('Now ready to handle fetches!');
       })
     );
 });

self.addEventListener('fetch', function(event) {
  event.respondWith(
      caches.match(event.request)
      .then(function(response) {
          // Cache hit - return response
          if (response) {
              return response;
          }
          return fetch(event.request);
      })
  );
});