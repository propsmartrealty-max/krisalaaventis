import os

silos = [
    "index.html",
    "krisala-aventis-tathawade-2-bhk-flats.html",
    "krisala-aventis-tathawade-3-bhk-luxury-apartments.html",
    "krisala-aventis-tathawade-flats-near-hinjewadi.html",
    "krisala-aventis-tathawade-construction-status.html",
    "tathawade-real-estate-investment-roi.html",
    "lifestyle-amenities-shopping-tathawade.html",
    "educational-hubs-near-krisala-aventis.html",
    "tathawade-connectivity-it-hubs.html",
    "krisala-legacy-pune-track-record-completed-projects.html",
    "aluform-technology-construction-quality-krisala-aventis.html",
    "public-transport-connectivity-tathawade-pune.html",
    "tathawade-real-estate-glossary.html",
    "tathawade-market-growth-calculator.html",
    "nri-investment-krisala-aventis-tathawade.html",
    "404.html"
]

base_dir = "/Users/vikasyewle/krisalaaventis"
google_verification = '<meta name="google-site-verification" content="HMzV9DNm0y-PepD-H3BpgrmZ2RshicvMwZ0V-Q8yBF4" />'

local_business_schema = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "RealEstateAgent",
    "name": "Krisala Aventis Tathawade",
    "image": "https://krisalaventis.in/assets/images/hero.png",
    "@id": "https://krisalaventis.in/#localbusiness",
    "url": "https://krisalaventis.in/",
    "telephone": "+917744009295",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Beside Shakai, Mumbai-Pune-Bangalore Highway, Tathawade",
      "addressLocality": "Pune",
      "postalCode": "411033",
      "addressRegion": "MH",
      "addressCountry": "IN"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 18.6298,
      "longitude": 73.7560
    },
    "openingHoursSpecification": {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
      ],
      "opens": "10:00",
      "closes": "19:00"
    },
    "sameAs": [
      "https://maps.app.goo.gl/TathawadeLocation",
      "https://www.facebook.com/KrisalaLegacy",
      "https://www.instagram.com/krisala_legacy"
    ]
  }
  </script>
"""

def total_google_lockdown(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): return

    with open(path, 'r') as f:
        content = f.read()

    # 1. Ensure Site Verification on all pages
    if 'name="google-site-verification"' not in content:
        content = content.replace('</title>', '</title>\n  ' + google_verification)

    # 2. Inject LocalBusiness (RealEstateAgent) Schema
    if 'RealEstateAgent' not in content:
        content = content.replace('</head>', local_business_schema + '</head>')

    with open(path, 'w') as f:
        f.write(content)
    print(f"Google Locked Down: {filename}")

for silo in silos:
    total_google_lockdown(silo)
