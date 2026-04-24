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
    "krisala-aventis-tathawade-price-list.html",
    "krisala-aventis-tathawade-brochure-download.html",
    "krisala-aventis-vs-competitors-tathawade.html",
    "vastu-compliance-krisala-aventis.html",
    "home-loan-emi-calculator-krisala-aventis.html"
]

base_dir = "/Users/vikasyewle/krisalaaventis"

# Mapping anchors to clean silo URLs
mapping = {
    '/#overview': '/krisala-aventis-tathawade-flats-near-hinjewadi',
    '#overview': '/krisala-aventis-tathawade-flats-near-hinjewadi',
    '/#floorplans': '/krisala-aventis-tathawade-2-bhk-flats',
    '#floorplans': '/krisala-aventis-tathawade-2-bhk-flats',
    '/#amenities': '/lifestyle-amenities-shopping-tathawade',
    '#amenities': '/lifestyle-amenities-shopping-tathawade',
    '/#location': '/tathawade-connectivity-it-hubs',
    '#location': '/tathawade-connectivity-it-hubs',
    '/#blog': '/tathawade-real-estate-glossary',
    '#blog': '/tathawade-real-estate-glossary',
    '/#legacy': '/krisala-legacy-pune-track-record-completed-projects',
    '#legacy': '/krisala-legacy-pune-track-record-completed-projects',
    '/#masterlayout': '/krisala-aventis-tathawade-construction-status',
    '#masterlayout': '/krisala-aventis-tathawade-construction-status'
}

def normalize_links(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): return

    with open(path, 'r') as f:
        content = f.read()

    # 1. Replace anchor links with clean URLs
    for anchor, clean in mapping.items():
        # Replace href="#anchor" with href="/clean"
        content = content.replace(f'href="{anchor}"', f'href="{clean}"')
    
    # 2. Final sweep for any .html links (just in case)
    content = re.sub(r'href="/([^"]+)\.html"', r'href="/\1"', content)

    with open(path, 'w') as f:
        f.write(content)
    print(f"Normalized navigation in {filename}")

for silo in silos:
    normalize_links(silo)
