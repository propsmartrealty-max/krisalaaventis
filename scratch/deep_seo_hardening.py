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

# 1. Update Sitemap
sitemap_path = os.path.join(base_dir, "sitemap.xml")
with open(sitemap_path, 'r') as f:
    sitemap_content = f.read()

new_urls = [
    "krisala-aventis-tathawade-price-list",
    "krisala-aventis-tathawade-brochure-download",
    "krisala-aventis-vs-competitors-tathawade",
    "vastu-compliance-krisala-aventis",
    "home-loan-emi-calculator-krisala-aventis"
]

for url in new_urls:
    if url not in sitemap_content:
        new_entry = f"""  <url>
    <loc>https://krisalaventis.in/{url}</loc>
    <lastmod>2026-04-23</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
"""
        sitemap_content = sitemap_content.replace('</urlset>', f"{new_entry}</urlset>")

with open(sitemap_path, 'w') as f:
    f.write(sitemap_content)

# 2. Update Service Worker
sw_path = os.path.join(base_dir, "sw.js")
with open(sw_path, 'r') as f:
    sw_content = f.read()

for url in new_urls:
    if f"'/{url}'" not in sw_content:
        sw_content = sw_content.replace("];", f"  ,'/{url}'\n];")

with open(sw_path, 'w') as f:
    f.write(sw_content)

# 3. Update Meta/Footer Keywords in Silos
for filename in silos:
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): continue

    with open(path, 'r') as f:
        content = f.read()

    # Add new silos to the Market Authority column if it exists
    if "Market Authority" in content:
        market_pattern = r'(<h5[^>]*>Market Authority</h5>\s*<ul[^>]*>)(.*?)(</ul>)'
        def add_market_links(match):
            links = match.group(2)
            for url in new_urls:
                if url not in links:
                    label = url.replace('krisala-aventis-', '').replace('-tathawade', '').replace('-', ' ').title()
                    links += f'            <li><a href="/{url}" style="color: #888; text-decoration: none;">{label}</a></li>\n'
            return match.group(1) + links + match.group(3)
        content = re.sub(market_pattern, add_market_links, content, flags=re.DOTALL)

    # Standardize footer back to home link
    content = content.replace('© 2026 Krisala Legacy | Part of the Krisala Aventis Tathawade Ecosystem', '© 2026 Krisala Legacy | <a href="/krisala-aventis-tathawade-price-list" style="color:inherit">Price List</a> | <a href="/krisala-aventis-tathawade-brochure-download" style="color:inherit">Brochure</a>')

    with open(path, 'w') as f:
        f.write(content)

print("Expansive Hardening Complete.")
