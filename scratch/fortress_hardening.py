import os
import re

base_dir = "/Users/vikasyewle/krisalaaventis"

all_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

def harden_html(content, filename):
    # 1. Add Preconnect/DNS-Prefetch for Google and Domain
    directives = """
  <link rel="dns-prefetch" href="https://fonts.googleapis.com">
  <link rel="dns-prefetch" href="https://fonts.gstatic.com">
  <link rel="dns-prefetch" href="https://www.googletagmanager.com">
  <link rel="preconnect" href="https://krisalaventis.in">
  <meta name="theme-color" content="#050608">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
"""
    if 'rel="dns-prefetch"' not in content:
        content = content.replace('</head>', directives + '</head>')

    # 2. Harden Image Alt Tags
    # Find images without alt or with generic alt
    pattern = r'<img([^>]*src="([^"]+)"[^>]*)>'
    
    def enrich_alt(match):
        attributes = match.group(1)
        src = match.group(2)
        if 'alt=' not in attributes or 'alt=""' in attributes:
            keyword = src.split('/')[-1].replace('.png', '').replace('.webp', '').replace('-', ' ').title()
            return f'<img{attributes} alt="Krisala Aventis Tathawade {keyword} — High-End Real Estate Pune">'
        return match.group(0)

    content = re.sub(pattern, enrich_alt, content)

    return content

for filename in all_files:
    path = os.path.join(base_dir, filename)
    with open(path, 'r') as f:
        content = f.read()
    
    new_content = harden_html(content, filename)
    
    if new_content != content:
        with open(path, 'w') as f:
            f.write(new_content)
        print(f"Hardened Head & Images: {filename}")

print("Total Fortress Hardening Complete.")
