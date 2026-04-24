import os
import re

mapping = {
    "tathawade-real-estate-investment-roi.html": "krisala-aventis-tathawade-investment-roi.html",
    "lifestyle-amenities-shopping-tathawade.html": "krisala-aventis-tathawade-amenities-lifestyle.html",
    "educational-hubs-near-krisala-aventis.html": "krisala-aventis-tathawade-educational-hubs.html",
    "tathawade-connectivity-it-hubs.html": "krisala-aventis-tathawade-connectivity-it-hubs.html",
    "krisala-legacy-pune-track-record-completed-projects.html": "krisala-aventis-tathawade-developer-legacy.html",
    "aluform-technology-construction-quality-krisala-aventis.html": "krisala-aventis-tathawade-aluform-technology.html",
    "public-transport-connectivity-tathawade-pune.html": "krisala-aventis-tathawade-public-transport.html",
    "tathawade-real-estate-glossary.html": "krisala-aventis-tathawade-real-estate-glossary.html",
    "tathawade-market-growth-calculator.html": "krisala-aventis-tathawade-market-growth-calculator.html",
    "nri-investment-krisala-aventis-tathawade.html": "krisala-aventis-tathawade-nri-investment.html",
    "vastu-compliance-krisala-aventis.html": "krisala-aventis-tathawade-vastu-compliance.html",
    "home-loan-emi-calculator-krisala-aventis.html": "krisala-aventis-tathawade-home-loan-emi-calculator.html",
    "krisala-aventis-vs-competitors-tathawade.html": "krisala-aventis-tathawade-competitor-comparison.html"
}

base_dir = "/Users/vikasyewle/krisalaaventis"

# 1. Rename files
for old, new in mapping.items():
    old_path = os.path.join(base_dir, old)
    new_path = os.path.join(base_dir, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old} -> {new}")

# 2. Update internal links in all files
all_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

# Create a clean URL mapping for link replacement
clean_mapping = {old.replace('.html', ''): new.replace('.html', '') for old, new in mapping.items()}

for filename in all_files:
    path = os.path.join(base_dir, filename)
    with open(path, 'r') as f:
        content = f.read()
    
    # Replace old links with new ones
    for old_url, new_url in clean_mapping.items():
        content = content.replace(f'href="/{old_url}"', f'href="/{new_url}"')
        content = content.replace(f'href="{old_url}.html"', f'href="{new_url}"')
    
    # Update canonical tags
    canonical_pattern = r'<link rel="canonical" href="https://krisalaventis\.in/([^"]+)">'
    def update_canonical(match):
        slug = match.group(1)
        if slug in clean_mapping:
            return f'<link rel="canonical" href="https://krisalaventis.in/{clean_mapping[slug]}">'
        return match.group(0)
    
    content = re.sub(canonical_pattern, update_canonical, content)

    with open(path, 'w') as f:
        f.write(content)

print("Keyword-Rich URL Refactor Complete.")
