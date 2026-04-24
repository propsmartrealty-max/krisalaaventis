import os
import random

silos = [f for f in os.listdir("/Users/vikasyewle/krisalaaventis") if f.endswith('.html') and f not in ['404.html', 'privacy-policy.html', 'terms-conditions.html']]

base_dir = "/Users/vikasyewle/krisalaaventis"

def get_title(content):
    import re
    match = re.search(r'<title>(.*?)</title>', content)
    return match.group(1).split('|')[0].strip() if match else "Explore More"

for filename in silos:
    path = os.path.join(base_dir, filename)
    with open(path, 'r') as f:
        content = f.read()
    
    if "Project Explorer" in content: continue

    # Pick 4 random silos (excluding current)
    others = [s for s in silos if s != filename]
    picks = random.sample(others, min(4, len(others)))

    links_html = ""
    for pick in picks:
        with open(os.path.join(base_dir, pick), 'r') as pf:
            p_content = pf.read()
        title = get_title(p_content)
        url = pick.replace('.html', '') if pick != 'index.html' else '/'
        links_html += f'        <a href="/{url}" style="background: rgba(202,163,80,0.05); padding: 15px; border-radius: 8px; border: 1px solid rgba(202,163,80,0.2); text-decoration: none; color: #fff; font-size: 0.9rem; transition: 0.3s;">{title} →</a>\n'

    explorer_section = f"""
  <!-- ======== PROJECT EXPLORER (Internal Link Velocity) ======== -->
  <section class="section related-silos" style="border-top: 1px solid var(--clr-glass-border); background: rgba(255,255,255,0.01);">
    <div class="container">
      <div class="section-tag">Project Explorer</div>
      <h3>Deep Dive <span class="gold">Intelligence.</span></h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 20px;">
{links_html}      </div>
    </div>
  </section>
"""
    # Inject before the footer
    if '<footer' in content:
        content = content.replace('<footer', explorer_section + '<footer')
    
    with open(path, 'w') as f:
        f.write(content)

print("Circular Silo Hardening Complete.")
