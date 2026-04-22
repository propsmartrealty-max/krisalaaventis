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
    "tathawade-market-growth-calculator.html"
]

base_dir = "/Users/vikasyewle/krisalaaventis"

def micro_optimize(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): return

    with open(path, 'r') as f:
        content = f.read()

    # 1. LCP Priority Hinting for Hero Images
    # Find the first image or hero background and add priority hints
    content = re.sub(r'(<img[^>]+src="[^"]*hero[^"]*"[^>]*>)', r'\1 fetchpriority="high"', content)
    
    # 2. Lazy Loading for non-hero images
    # Add loading="lazy" to images that don't have it and aren't hero images
    def add_lazy(match):
        img_tag = match.group(0)
        if 'loading=' not in img_tag and 'hero' not in img_tag:
            return img_tag.replace('>', ' loading="lazy">')
        return img_tag

    content = re.sub(r'<img[^>]+>', add_lazy, content)

    # 3. Voice Search Hardening (Speakable Schema)
    voice_schema = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "Krisala Aventis Official Portal",
    "speakable": {
      "@type": "SpeakableSpecification",
      "xpath": [
        "/html/head/title",
        "/html/head/meta[@name='description']/@content"
      ]
    },
    "url": "https://krisalaventis.in/"
  }
  </script>
"""
    if 'SpeakableSpecification' not in content:
        content = content.replace('</head>', voice_schema + '</head>')

    with open(path, 'w') as f:
        f.write(content)
    print(f"Micro-Optimized: {filename}")

for silo in silos:
    micro_optimize(silo)
