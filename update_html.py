import os
import glob

# HTML chunks to replace
old_font = """<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500;600;700&family=Lato:wght@300;400;700&display=swap" rel="stylesheet" />"""
new_font = """<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />"""

old_logo_blue = """<div class="logo-icon" aria-hidden="true">
          <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M8 4C8 4 6 8 6 14C6 18 8 21 12 22L12 28H20V22C24 21 26 18 26 14C26 8 24 4 24 4" stroke="#0369A1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M12 14H20M16 10V18" stroke="#0369A1" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </div>"""
        
old_logo_light = """<div class="logo-icon" aria-hidden="true">
            <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8 4C8 4 6 8 6 14C6 18 8 21 12 22L12 28H20V22C24 21 26 18 26 14C26 8 24 4 24 4" stroke="#60A5FA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M12 14H20M16 10V18" stroke="#60A5FA" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </div>"""

# Check for slightly different indentation on footer logo, just matching the div content
old_logo_blue_inner = """<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M8 4C8 4 6 8 6 14C6 18 8 21 12 22L12 28H20V22C24 21 26 18 26 14C26 8 24 4 24 4" stroke="#0369A1" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M12 14H20M16 10V18" stroke="#0369A1" stroke-width="2" stroke-linecap="round"/>
          </svg>"""

old_logo_light_inner = """<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8 4C8 4 6 8 6 14C6 18 8 21 12 22L12 28H20V22C24 21 26 18 26 14C26 8 24 4 24 4" stroke="#60A5FA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M12 14H20M16 10V18" stroke="#60A5FA" stroke-width="2" stroke-linecap="round"/>
            </svg>"""

new_logo = """<div class="logo-monogram" aria-hidden="true">
          <span>A</span>
        </div>"""

for file in glob.glob("*.html"):
    with open(file, "r") as f:
        content = f.read()
    
    # 1. Replace fonts
    content = content.replace(old_font, new_font)
    
    # 2. Replace logos
    if old_logo_blue in content:
        content = content.replace(old_logo_blue, new_logo)
    
    # Let's cleanly replace the footer logo wrapper
    footer_logo = """<div class="logo-icon" aria-hidden="true">\n            <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">\n              <path d="M8 4C8 4 6 8 6 14C6 18 8 21 12 22L12 28H20V22C24 21 26 18 26 14C26 8 24 4 24 4" stroke="#60A5FA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>\n              <path d="M12 14H20M16 10V18" stroke="#60A5FA" stroke-width="2" stroke-linecap="round"/>\n            </svg>\n          </div>"""
    new_footer_logo = """<div class="logo-monogram" aria-hidden="true">\n            <span>A</span>\n          </div>"""
    
    content = content.replace(footer_logo, new_footer_logo)
    
    # 3. For index.html specifically: Hero tweaks
    if file == "index.html":
        # Add eyebrow
        content = content.replace("<h1 class=\"hero-title\">", "<span class=\"hero-eyebrow\">Calgary Plumbing Services</span>\n      <h1 class=\"hero-title\">")
        # Enhance heading
        content = content.replace("<h1 class=\"hero-title\">Calgary's Trusted Plumbing, Heating &amp; Gas Specialists</h1>", "<h1 class=\"hero-title\">Calgary's Trusted Plumbing,\n      <em>Heating &amp; Gas</em> Specialists</h1>")
        # Change button classes
        content = content.replace("class=\"btn btn-primary\" id=\"hero-call-btn\"", "class=\"btn-hero-primary\" id=\"hero-call-btn\"")
        content = content.replace("class=\"btn btn-outline\" id=\"hero-services-btn\"", "class=\"btn-hero-outline\" id=\"hero-services-btn\"")

    with open(file, "w") as f:
        f.write(content)
print("Updated HTML files.")
