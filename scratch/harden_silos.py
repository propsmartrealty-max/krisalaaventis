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
    "krisala-aventis-tathawade-price-list.html",
    "krisala-aventis-tathawade-brochure-download.html",
    "krisala-aventis-vs-competitors-tathawade.html",
    "vastu-compliance-krisala-aventis.html",
    "home-loan-emi-calculator-krisala-aventis.html"
]

base_dir = "/Users/vikasyewle/krisalaaventis"

# Footer link block to inject/update
new_footer_links = """
          <div class="footer-links">
            <a href="/krisala-aventis-tathawade-2-bhk-flats">2 BHK Flats</a>
            <a href="/krisala-aventis-tathawade-3-bhk-luxury-apartments">3 BHK Flats</a>
            <a href="/krisala-aventis-tathawade-price-list">Price List</a>
            <a href="/krisala-aventis-tathawade-brochure-download">Brochure Download</a>
            <a href="/krisala-aventis-tathawade-construction-status">Construction Status</a>
            <a href="/tathawade-real-estate-investment-roi">ROI Analysis</a>
            <a href="/lifestyle-amenities-shopping-tathawade">Amenities</a>
            <a href="/educational-hubs-near-krisala-aventis">Education Hubs</a>
            <a href="/tathawade-connectivity-it-hubs">Connectivity</a>
            <a href="/krisala-legacy-pune-track-record-completed-projects">Legacy</a>
            <a href="/aluform-technology-construction-quality-krisala-aventis">Technology</a>
            <a href="/public-transport-connectivity-tathawade-pune">Public Transport</a>
            <a href="/tathawade-real-estate-glossary">Glossary</a>
            <a href="/tathawade-market-growth-calculator">Growth Calculator</a>
            <a href="/nri-investment-krisala-aventis-tathawade">NRI Investment</a>
            <a href="/krisala-aventis-vs-competitors-tathawade">Competitor Comparison</a>
            <a href="/vastu-compliance-krisala-aventis">Vastu Compliance</a>
            <a href="/home-loan-emi-calculator-krisala-aventis">EMI Calculator</a>
          </div>
"""

def update_footer(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path): return

    with open(path, 'r') as f:
        content = f.read()

    # Look for the footer-links div and replace it
    import re
    pattern = r'<div class="footer-links">.*?</div>'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_footer_links.strip(), content, flags=re.DOTALL)
        with open(path, 'w') as f:
            f.write(content)
        print(f"Updated footer in {filename}")
    else:
        print(f"Could not find footer links in {filename}")

for silo in silos:
    update_footer(silo)
