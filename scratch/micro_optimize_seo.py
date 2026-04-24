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
    "nri-investment-krisala-aventis-tathawade.html"
]

base_dir = "/Users/vikasyewle/krisalaaventis"

# Dimensions for CLS optimization
dimensions = {
    "hero.png": (1024, 555),
    "floorplan-2bhk.png": (1024, 566),
    "floorplan-3bhk.png": (1024, 558),
    "interior.png": (1024, 1024),
    "location-infographic.png": (1024, 1024),
    "amenities-infographic.png": (1024, 1024),
    "logo.png": (1024, 1024),
    "master-layout.png": (1024, 561)
}

def optimize_file(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): return

    with open(path, 'r') as f:
        content = f.read()

    # 1. Fix fetchpriority syntax error: "> fetchpriority="high"" -> " fetchpriority="high">"
    content = content.replace('> fetchpriority="high"', ' fetchpriority="high">')

    # 2. Add dimensions to images that don't have them
    for img_name, dims in dimensions.items():
        w, h = dims
        # Look for the img tag with the src
        pattern = rf'(<img[^>]*src="[^"]*{img_name}"[^>]*)(>)'
        
        def add_dims(match):
            tag_content = match.group(1)
            if 'width=' not in tag_content:
                tag_content += f' width="{w}" height="{h}"'
            return tag_content + match.group(2)

        content = re.sub(pattern, add_dims, content)

    # 3. Fix internal links: ensure they are clean (no .html) in footer matrix
    # pattern: href="/krisala-aventis-tathawade-2-bhk-flats.html" -> "/krisala-aventis-tathawade-2-bhk-flats"
    content = re.sub(r'href="/([^"]+)\.html"', r'href="/\1"', content)

    # 4. Remove duplicate Organization schema if present (only for silos where it might have been copied)
    # (Optional: this is safer to do manually or with more precise regex)

    with open(path, 'w') as f:
        f.write(content)
    print(f"Optimized: {filename}")

for silo in silos:
    optimize_file(silo)
