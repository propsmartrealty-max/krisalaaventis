import os
import re

base_dir = "/Users/vikasyewle/krisalaaventis"
base_url = "https://krisalaventis.in"

# 1. Get all HTML files (clean)
silos = [f.replace('.html', '') for f in os.listdir(base_dir) if f.endswith('.html') and f not in ['404.html', 'privacy-policy.html', 'terms-conditions.html']]
silos.sort()

# 2. Update Sitemap
sitemap_urls = []
for silo in silos:
    priority = "1.0" if silo == 'index' else "0.9"
    url = f"{base_url}/" if silo == 'index' else f"{base_url}/{silo}"
    sitemap_urls.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-04-23</lastmod>
    <changefreq>{"daily" if silo == 'index' else "weekly"}</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
{"".join(sitemap_urls)}
</urlset>"""

with open(os.path.join(base_dir, "sitemap.xml"), 'w') as f:
    f.write(sitemap_content)

# 3. Update Service Worker
sw_assets = [f"'/{silo}'" if silo != 'index' else "'/'" for silo in silos]
sw_assets.extend(["'/assets/css/style.css'", "'/assets/js/script.js'", "'/favicon.png'"])

sw_content = f"""const CACHE_NAME = 'krisala-aventis-v3';
const ASSETS = [
  {",\n  ".join(sw_assets)}
];

self.addEventListener('install', (event) => {{
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {{
      return cache.addAll(ASSETS);
    }})
  );
}});

self.addEventListener('activate', (event) => {{
  event.waitUntil(
    caches.keys().then((keys) => {{
      return Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)));
    }})
  );
}});

self.addEventListener('fetch', (event) => {{
  event.respondWith(
    caches.match(event.request).then((response) => {{
      return response || fetch(event.request);
    }})
  );
}});
"""
with open(os.path.join(base_dir, "sw.js"), 'w') as f:
    f.write(sw_content)

# 4. Update Indexing Script
indexing_urls = [f"'{base_url}/'" if silo == 'index' else f"'{base_url}/{silo}'" for silo in silos]
push_path = os.path.join(base_dir, "indexing-automation/index-push.js")
with open(push_path, 'r') as f:
    push_content = f.read()

push_content = re.sub(r'const urls = \[.*?\];', f"const urls = [\n  {',\\n  '.join(indexing_urls)}\n];", push_content, flags=re.DOTALL)
with open(push_path, 'w') as f:
    f.write(push_content)

print("Ecosystem Sync Complete.")
