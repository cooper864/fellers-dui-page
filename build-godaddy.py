"""Build the GoDaddy custom-code versions of a page.

GoDaddy's custom code block goes inside <body> and is limited to 51,000 characters,
so this strips the document wrapper, points images at jsDelivr, opens links in the
main window, drops the sticky call bar, and writes one paste-ready block per page.

Usage: python3 build-godaddy.py            (builds every page in PAGES)
"""
import re

REPO = "https://cdn.jsdelivr.net/gh/cooper864/fellers-dui-page@"
LIMIT = 51000

# page source -> (commit holding its images/web files, image folder in the repo, output prefix)
PAGES = {
    "index.html": ("0bc5021a0de6667c437d954d962de38881b2860c", "images/web/", ""),
    "weapons/index.html": ("4bb4090c0d197e008c94818e0b2c5275b64b3c3b", "weapons/images/web/", "weapons/"),
}


def build(src, commit, image_dir, out):
    s = open(src).read()
    s = s.replace('src="images/', f'src="{REPO}{commit}/{image_dir}')
    s = re.sub(r'\n  <!-- STICKY MOBILE CALL BAR -->.*?\n  </div>\n', "\n", s, flags=re.S)
    s = s.replace(" padding-bottom: 76px;", "")
    s = re.sub(r"<a (?!target)", '<a target="_top" ', s)

    fonts = re.search(r'<link href="https://fonts.googleapis.com[^>]*>', s).group(0)
    style = re.search(r"<style>.*?</style>", s, re.S).group(0)
    body = re.search(r'<div class="fl-dui">(.*)</div>\s*</body>', s, re.S).group(1)
    sections = [x.strip() for x in re.split(r"\n  (?=<!-- [A-Z0-9][A-Z0-9 ]+ -->)", body) if x.strip()]

    head = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            f"{fonts}\n{style}\n")

    def block(secs):
        return head + '<div class="fl-dui">\n  ' + "\n\n  ".join(secs) + "\n</div>\n"

    outputs = {f"{out}godaddy-body.html": block(sections)}
    for path, text in outputs.items():
        assert len(text) < LIMIT, (path, len(text))
        open(path, "w").write(text)
        print(f"{path}: {len(text):,} chars")


for src, (commit, image_dir, out) in PAGES.items():
    build(src, commit, image_dir, out)
