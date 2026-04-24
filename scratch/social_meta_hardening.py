import os
import re

base_dir = "/Users/vikasyewle/krisalaaventis"

all_files = [f for f in os.listdir(base_dir) if f.endswith('.html') and f not in ['404.html']]

def get_best_og(filename, content):
    title_match = re.search(r'<title>(.*?)</title>', content)
    title = title_match.group(1).split('|')[0].strip() if title_match else "Krisala Aventis"
    
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
    desc = desc_match.group(1) if desc_match else "Luxury 2.25 & 3.25 BHK Apartments in Tathawade, Pune."

    og_tags = f"""
  <meta property="og:site_name" content="Krisala Aventis Tathawade">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://krisalaventis.in/{filename.replace('.html', '')}">
  <meta property="og:image" content="https://krisalaventis.in/assets/images/hero.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://krisalaventis.in/assets/images/hero.png">
"""
    return og_tags

for filename in all_files:
    path = os.path.join(base_dir, filename)
    with open(path, 'r') as f:
        content = f.read()
    
    if 'property="og:site_name"' in content: continue

    og_tags = get_best_og(filename, content)
    
    # Replace existing OG tags if they exist, or inject new ones
    if 'property="og:title"' in content:
        content = re.sub(r'<meta property="og:.*?>', '', content)
        content = re.sub(r'<meta name="twitter:.*?>', '', content)
    
    # Inject after the canonical tag
    content = re.sub(r'(<link rel="canonical" .*?>)', r'\1' + og_tags, content)

    with open(path, 'w') as f:
        f.write(content)

print("Social Meta Hardening Complete.")
