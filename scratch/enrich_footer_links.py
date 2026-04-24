import os
import re

base_dir = "/Users/vikasyewle/krisalaaventis"

all_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

for filename in all_files:
    path = os.path.join(base_dir, filename)
    with open(path, 'r') as f:
        content = f.read()
    
    # Identify footer links and update their text to be keyword rich
    # example: <a href="/krisala-aventis-tathawade-price-list" ...>Price List</a>
    # -> <a href="/krisala-aventis-tathawade-price-list" ...>Krisala Aventis Price List</a>
    
    pattern = r'(<a href="/(krisala-aventis-tathawade-[^"]+)"[^>]*>)([^<]+)(</a>)'
    
    def enrich_link_text(match):
        prefix = match.group(1)
        slug = match.group(2)
        old_text = match.group(3).strip()
        suffix = match.group(4)
        
        if "Krisala Aventis" not in old_text:
            new_text = f"Krisala Aventis {old_text}"
            return f"{prefix}{new_text}{suffix}"
        return match.group(0)

    content = re.sub(pattern, enrich_link_text, content)

    with open(path, 'w') as f:
        f.write(content)

print("Footer Link Text Enriched.")
