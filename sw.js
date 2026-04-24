const CACHE_NAME = 'krisala-aventis-v3';
const ASSETS = [
  '/',
  '/krisala-aventis-tathawade-2-bhk-flats',
  '/krisala-aventis-tathawade-3-bhk-luxury-apartments',
  '/krisala-aventis-tathawade-aluform-technology',
  '/krisala-aventis-tathawade-amenities-lifestyle',
  '/krisala-aventis-tathawade-brochure-download',
  '/krisala-aventis-tathawade-competitor-comparison',
  '/krisala-aventis-tathawade-connectivity-it-hubs',
  '/krisala-aventis-tathawade-construction-status',
  '/krisala-aventis-tathawade-cost-sheet-estimator',
  '/krisala-aventis-tathawade-customer-reviews-testimonials',
  '/krisala-aventis-tathawade-developer-legacy',
  '/krisala-aventis-tathawade-educational-hubs',
  '/krisala-aventis-tathawade-flats-near-hinjewadi',
  '/krisala-aventis-tathawade-growth-story-roi-2026',
  '/krisala-aventis-tathawade-home-loan-emi-calculator',
  '/krisala-aventis-tathawade-investment-roi',
  '/krisala-aventis-tathawade-lifestyle-it-park-proximity',
  '/krisala-aventis-tathawade-luxury-specifications-aluform',
  '/krisala-aventis-tathawade-market-growth-calculator',
  '/krisala-aventis-tathawade-near-jspm-university',
  '/krisala-aventis-tathawade-near-mumbai-pune-expressway',
  '/krisala-aventis-tathawade-near-phoenix-mall-wakad',
  '/krisala-aventis-tathawade-nri-investment',
  '/krisala-aventis-tathawade-price-list',
  '/krisala-aventis-tathawade-public-transport',
  '/krisala-aventis-tathawade-real-estate-glossary',
  '/krisala-aventis-tathawade-vastu-compliance',
  '/sitemap-html',
  '/assets/css/style.css',
  '/assets/js/script.js',
  '/favicon.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS);
    })
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)));
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});
