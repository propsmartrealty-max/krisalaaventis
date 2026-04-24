import os
import re

base_dir = "/Users/vikasyewle/krisalaaventis"

all_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

def harden_performance(content):
    # 1. Lazy Loading & Async Decoding for non-hero images
    # We first identify hero images (usually the first img or those in silo-hero)
    # Then we add loading="lazy" and decoding="async" to others.
    
    pattern = r'<img([^>]+)>'
    
    def process_img(match):
        attrs = match.group(1)
        # Skip if it's already got loading or if it's a hero image
        if 'hero.png' in attrs or 'logo.png' in attrs or 'fetchpriority="high"' in attrs:
            if 'fetchpriority="high"' not in attrs and 'hero.png' in attrs:
                return f'<img{attrs} fetchpriority="high" decoding="async">'
            return match.group(0)
        
        # Add lazy loading and async decoding
        if 'loading=' not in attrs:
            attrs += ' loading="lazy"'
        if 'decoding=' not in attrs:
            attrs += ' decoding="async"'
        
        return f'<img{attrs}>'

    content = re.sub(pattern, process_img, content)
    
    # 2. Add resource hints for the domain itself
    if 'rel="preconnect" href="https://krisalaventis.in"' not in content:
        content = content.replace('</head>', '  <link rel="preconnect" href="https://krisalaventis.in">\n</head>', 1)

    return content

for filename in all_files:
    path = os.path.join(base_dir, filename)
    with open(path, 'r') as f:
        content = f.read()
    
    new_content = harden_performance(content)
    
    if new_content != content:
        with open(path, 'w') as f:
            f.write(new_content)
        print(f"Performance Hardened: {filename}")

print("Phase 7: Image & Resource Hardening Complete.")
