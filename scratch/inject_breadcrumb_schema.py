import os
import re

base_dir = "/Users/vikasyewle/krisalaaventis"
base_url = "https://krisalaventis.in"

all_files = [f for f in os.listdir(base_dir) if f.endswith('.html') and f not in ['404.html']]

def get_page_title(content):
    match = re.search(r'<title>(.*?)</title>', content)
    if match:
        return match.group(1).split('|')[0].strip()
    return "Krisala Aventis"

for filename in all_files:
    path = os.path.join(base_dir, filename)
    with open(path, 'r') as f:
        content = f.read()
    
    if "BreadcrumbList" in content: continue

    page_title = get_page_title(content)
    slug = filename.replace('.html', '')
    url = f"{base_url}/" if slug == 'index' else f"{base_url}/{slug}"

    breadcrumb_schema = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "{base_url}/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Krisala Aventis Tathawade",
        "item": "{base_url}/"
      }}{"" if slug == 'index' else f""",
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{page_title}",
        "item": "{url}"
      }}"""}
    ]
  }}
  </script>
"""
    # Inject before the first </head>
    content = content.replace('</head>', f"{breadcrumb_schema}</head>")

    with open(path, 'w') as f:
        f.write(content)

print("Breadcrumb Schema Injection Complete.")
