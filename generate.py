#!/usr/bin/env python3
"""Regenerate api/display and index.html from the openobject-gallery-N image files here.

Run this after adding, removing, or replacing images, then commit and push:

    python3 generate.py

The OpenObject apps are dumb clients: they fetch /api/display and play whatever it
names. So this script is the only "wiring" needed for any number of pieces. It finds
every openobject-gallery-N.(jpg|jpeg|png), sorts them numerically (so -10 follows -9),
and writes the rotation. Pace and order are the two constants below.
"""
import json, re, glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
DURATION_MS = 8000   # one global equal-time duration (ms) for every piece
MODE = "sequence"    # "sequence" (fixed numeric order) or "shuffle"

EXT_FORMAT = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png"}


def pieces():
    found = []
    for path in glob.glob(os.path.join(HERE, "openobject-gallery-*.*")):
        name = os.path.basename(path)
        m = re.fullmatch(r"openobject-gallery-(\d+)\.(jpg|jpeg|png)", name, re.IGNORECASE)
        if m:
            found.append((int(m.group(1)), name, EXT_FORMAT[m.group(2).lower()]))
    found.sort(key=lambda t: t[0])  # numeric, so -10 follows -9 (not lexical)
    return found


def write_api_display(items):
    payload = {
        "items": [
            {"id": n, "kind": "still", "format": fmt, "fit": "fit", "src": "/" + name}
            for (n, name, fmt) in items
        ],
        "durationMs": DURATION_MS,
        "mode": MODE,
        "pinnedId": None,
        "asleep": False,
        "source": "library",
    }
    os.makedirs(os.path.join(HERE, "api"), exist_ok=True)
    with open(os.path.join(HERE, "api", "display"), "w") as f:
        json.dump(payload, f, indent=2)
        f.write("\n")


def write_index(items):
    imgs = "\n    ".join(
        f'<img src="/{name}" alt="OpenObject" loading="lazy">' for (_, name, _) in items
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>OpenObject Gallery</title>
  <style>
    :root {{ color-scheme: dark; }}
    html, body {{ margin: 0; background: #000; color: #fff;
      font-family: -apple-system, system-ui, Segoe UI, Roboto, Helvetica, Arial, sans-serif; }}
    main {{ max-width: 1100px; margin: 0 auto; padding: 32px; display: flex; flex-direction: column;
      align-items: center; gap: 18px; text-align: center; box-sizing: border-box; }}
    img {{ width: 100%; height: auto; border-radius: 8px; }}
    h1 {{ font-size: 1.1rem; font-weight: 600; letter-spacing: 0.02em; margin: 8px 0 0; }}
    p {{ margin: 0 0 12px; color: #9a9a9a; font-size: 0.95rem; line-height: 1.5; }}
    a {{ color: #fff; }}
  </style>
</head>
<body>
  <main>
    <h1>OpenObject Gallery</h1>
    <p>A public sample gallery for the OpenObject apps. Open the OpenObject app on your Apple TV,
       iPad, or iPhone with no Host on your network, and choose OpenObject Gallery to see these
       pieces rotate. Learn more at <a href="https://openobject.io">openobject.io</a>.</p>
    {imgs}
  </main>
</body>
</html>
"""
    with open(os.path.join(HERE, "index.html"), "w") as f:
        f.write(html)


def main():
    items = pieces()
    if not items:
        raise SystemExit("no openobject-gallery-N.(jpg|jpeg|png) files found")
    write_api_display(items)
    write_index(items)
    nums = [n for (n, _, _) in items]
    print(f"wrote api/display + index.html for {len(items)} pieces: {nums}")


if __name__ == "__main__":
    main()
