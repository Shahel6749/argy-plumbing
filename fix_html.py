import glob, os

for f in glob.glob('*.html'):
    with open(f, 'r') as file:
        content = file.read()
    
    # SVG favicon
    if '<link rel="icon"' not in content:
        content = content.replace(
            '<link rel="stylesheet" href="styles.css" />',
            '<link rel="icon" type="image/svg+xml" href="images/logo.svg" />\n  <link rel="stylesheet" href="styles.css" />'
        )

    # Logo monogram -> image
    content = content.replace(
        '<div class="logo-monogram" aria-hidden="true">\n          <span>A</span>\n        </div>',
        '<img src="images/logo.svg" alt="" class="logo-image" aria-hidden="true" />'
    )
    content = content.replace(
        '<div class="logo-monogram" aria-hidden="true">\n            <span>A</span>\n          </div>',
        '<img src="images/logo.svg" alt="" class="logo-image" aria-hidden="true" />'
    )
    
    # footer exact match removal
    content = content.replace(
        '<p>Calgary\'s trusted plumbing, heating &amp; gas fitting company. Women-owned. 5-star rated.</p>',
        '<p>Calgary\'s trusted plumbing, heating &amp; gas fitting company. 5-star rated.</p>'
    )
    
    with open(f, 'w') as file:
        file.write(content)
