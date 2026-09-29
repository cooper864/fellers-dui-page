# Fellers Law – Virginia Beach DUI Page Redesign

Redesign of the content on https://fellers-law.com/dui-lawyer-1, from
"Facing a DUI in Virginia Beach? Don't Leave Your Future to Chance." down to the footer.
All original copy is kept; the goal of the layout is to drive phone calls to (757) 990-3138.

## Files
- `index.html` – the full section (HTML + scoped CSS, everything under `.fl-dui`)
- `images/attorneys-courtroom.jpg` – hero photo
- `images/attorney-headshot.jpg` – "What Sets Us Apart" portrait
- `images/traffic-stop-guide-cover.jpg` – cover for the traffic-stop blog post card

## Page flow
1. Hero – headline, intro copy, gold "Call" button, attorneys photo, "Former Prosecutors" badge
2. Trust strip
3. What to Do After a DUI Arrest – numbered step cards + evidence callout
4. What Sets Us Apart – headshot, pull quote, "Talk to Us" call button
5. Why Local Experience Matters
6. Related guide card → "How to Assert Your Rights During a Virginia Traffic Stop"
7. Final call-to-action with large tap-to-call number
8. Sticky "Call Now" bar on phones

## Using it on the site
Upload the three images to the site's media library and replace the `images/...`
paths in `index.html` with the hosted image URLs. Paste everything inside `<body>`
plus the `<style>` block (and the Google Fonts `<link>`) into the page or an HTML embed.

## GoDaddy version
`godaddy-embed.html` is a paste-ready copy for GoDaddy Website Builder's HTML section:
photos are compressed and embedded in the file (no uploads needed), links open in the
main window (`target="_top"`), and the sticky mobile call bar is removed because it
can't stay on screen inside GoDaddy's embed frame.
