const { google } = require('googleapis');
const fs = require('fs');
const path = require('path');

/**
 * SOVEREIGN INDEXING ENGINE v2.0
 * Optimized for Krisala Aventis Rationalized Apex Infrastructure
 * 
 * Target: 100% Indexing Coverage in 24 Hours
 */

const keyFile = path.join(__dirname, 'service-account.json');
const urls = [
  'https://krisalaventis.in/',
  'https://krisalaventis.in/krisala-aventis-tathawade-2-bhk-flats',
  'https://krisalaventis.in/krisala-aventis-tathawade-3-bhk-luxury-apartments',
  'https://krisalaventis.in/krisala-aventis-tathawade-construction-status',
  'https://krisalaventis.in/tathawade-real-estate-investment-roi',
  'https://krisalaventis.in/lifestyle-amenities-shopping-tathawade',
  'https://krisalaventis.in/educational-hubs-near-krisala-aventis',
  'https://krisalaventis.in/tathawade-connectivity-it-hubs.html'
];

async function pushToIndex() {
  if (!fs.existsSync(keyFile)) {
    console.error('\x1b[31m❌ Error: service-account.json not found.\x1b[0m');
    console.log('\x1b[33mTo activate indexing dominance, please follow the setup guide and deploy your Google JSON key.\x1b[0m');
    return;
  }

  const jwtClient = new google.auth.JWT(
    null,
    keyFile,
    null,
    ['https://www.googleapis.com/auth/indexing'],
    null
  );

  try {
    await jwtClient.authorize();
    console.log('\x1b[32m✅ Authorized with Google Indexing API\x1b[0m');

    const indexing = google.indexing('v3');

    for (const url of urls) {
      const res = await indexing.urlNotifications.publish({
        auth: jwtClient,
        requestBody: {
          url: url,
          type: 'URL_UPDATED'
        }
      });
      console.log(`🚀 \x1b[36mIndexing Pushed:\x1b[0m ${url} [Status: ${res.status}]`);
      
      // Delay to respect API quota
      await new Promise(resolve => setTimeout(resolve, 500));
    }
    
    print('\x1b[32m✨ All high-intent URLs pushed to Google Search Console.\x1b[0m');
  } catch (err) {
    console.error('\x1b[31m⚠️ Fatal API Error:\x1b[0m', err.message);
  }
}

pushToIndex().catch(console.error);
