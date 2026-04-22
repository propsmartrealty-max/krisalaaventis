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
honeypot_html = '<input type="checkbox" name="contact_me" style="display:none !important" tabindex="-1" autocomplete="off">'

def harden_forms(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): return

    with open(path, 'r') as f:
        content = f.read()

    # 1. Inject Honeypot into all forms
    if 'name="contact_me"' not in content:
        content = content.replace('<form', '<form') # just ensuring we find it
        content = re.sub(r'(<form[^>]*>)', r'\1\n              ' + honeypot_html, content)

    # 2. Add Prefetch/Preconnect for Security and Speed
    preconnects = """
  <link rel="preconnect" href="https://api.web3forms.com">
  <link rel="preconnect" href="https://api.qrserver.com">
"""
    if 'api.web3forms.com' not in content:
        content = content.replace('</head>', preconnects + '</head>')

    with open(path, 'w') as f:
        f.write(content)
    print(f"Fortified: {filename}")

for silo in silos:
    harden_forms(silo)
