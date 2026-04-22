import os
import re

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

# GTM Block Pattern
gtm_pattern = r'<!-- Google Tag Manager.*?End Google Tag Manager -->'

def final_master_polish(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): return

    with open(path, 'r') as f:
        content = f.read()

    # 1. Update Language Localization
    content = content.replace('<html lang="en">', '<html lang="en-IN">')

    # 2. Remove hardcoded GTM blocks (config.js handles it now)
    content = re.sub(gtm_pattern, '', content, flags=re.DOTALL)
    
    # Also remove GTM noscript if present
    content = re.sub(r'<!-- Google Tag Manager \(noscript\).*?End Google Tag Manager \(noscript\) -->', '', content, flags=re.DOTALL)

    # 3. Add SearchBox Schema to Index
    if filename == "index.html" and 'SearchAction' not in content:
        search_schema = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "url": "https://krisalaventis.in/",
    "potentialAction": {
      "@type": "SearchAction",
      "target": "https://krisalaventis.in/#contact?q={search_term_string}",
      "query-input": "required name=search_term_string"
    }
  }
  </script>
"""
        content = content.replace('</head>', search_schema + '</head>')

    with open(path, 'w') as f:
        f.write(content)
    print(f"Master Polished: {filename}")

for silo in silos:
    final_master_polish(silo)
