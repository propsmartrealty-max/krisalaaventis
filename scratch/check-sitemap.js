const fs = require('fs');

const sitemap = fs.readFileSync('sitemap.xml', 'utf8');
const index = fs.readFileSync('index.html', 'utf8');

const urls = sitemap.match(/<loc>https:\/\/krisalaventis\.in\/([^<]+)<\/loc>/g)
    .map(u => u.replace('<loc>https://krisalaventis.in/', '').replace('</loc>', ''))
    .filter(u => u !== '');

console.log('--- Silo Link Audit ---');
urls.forEach(url => {
    const isLinked = index.includes(url);
    console.log(`${isLinked ? '✅' : '❌'} ${url}`);
});
