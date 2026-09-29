"""Build the GoDaddy custom-code versions of index.html.

GoDaddy's custom code block goes inside <body> and is limited to 51,000 characters,
so this strips the document wrapper, points images at jsDelivr, opens links in the
main window, drops the sticky call bar, and writes a one-block and a two-part version.
"""
import re

CDN = "https://cdn.jsdelivr.net/gh/cooper864/fellers-dui-page@0bc5021a0de6667c437d954d962de38881b2860c/images/web/"
LIMIT = 51000

s = open("index.html").read()
s = s.replace('src="images/', f'src="{CDN}')
s = re.sub(r'\n  <!-- STICKY MOBILE CALL BAR -->.*?\n  </div>\n', "\n", s, flags=re.S)
s = s.replace(" padding-bottom: 76px;", "")
s = re.sub(r"<a (?!target)", '<a target="_top" ', s)

fonts = re.search(r'<link href="https://fonts.googleapis.com[^>]*>', s).group(0)
style = re.search(r"<style>.*?</style>", s, re.S).group(0)
body = re.search(r'<div class="fl-dui">(.*)</div>\s*</body>', s, re.S).group(1)
sections = [x.strip() for x in re.split(r"\n  (?=<!-- [A-Z][A-Z ]+ -->)", body) if x.strip()]

head = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        f"{fonts}\n{style}\n")

def block(secs):
    return head + '<div class="fl-dui">\n  ' + "\n\n  ".join(secs) + "\n</div>\n"

outputs = {
    "godaddy-body.html": block(sections),
    "godaddy-parts/part-1.html": block(sections[:3]),
    "godaddy-parts/part-2.html": block(sections[3:]),
}
for path, text in outputs.items():
    assert len(text) < LIMIT, (path, len(text))
    open(path, "w").write(text)
    print(f"{path}: {len(text):,} chars")
