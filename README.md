# OpenObject Gallery

The public sample Host behind **https://gallery.openobject.io**, served as a static
site on GitHub Pages. The OpenObject apps (Apple TV, iPad, iPhone) offer it in the
Host picker's empty state (when no Host is found on the network), so a new owner, or
an App Store reviewer, can see real art immediately without running a Host of their own.

An OpenObject display is a dumb client: it fetches `/api/display` and then the media
that response names. So this repo just serves those things statically:

- `openobject-gallery-1.jpg`, `-2.jpg`, ... — the artwork the rotation cycles through.
  Names are a simple numeric convention; drop in `openobject-gallery-<N>.jpg` and it
  joins the rotation in numeric order. Keep them right-sized (~3840px wide is plenty —
  the apps decode at 3840 max and fit to screen).
- `api/display` — the rotation (JSON), **generated** from the image files (see below).
- `index.html` — a plain landing page listing the pieces, also generated.
- `CNAME` / `.nojekyll` — bind the site to `gallery.openobject.io` and serve files as-is.

## Changing the art

1. Add, remove, or replace any `openobject-gallery-<N>.jpg` files.
2. Regenerate the rotation:

   ```
   python3 generate.py
   ```

   It scans every `openobject-gallery-N.(jpg|jpeg|png)`, sorts them numerically (so
   `-10` follows `-9`), and rewrites `api/display` + `index.html`. No hand-editing.
3. Commit and push. The apps pick up the change on their next poll; no app change and
   no App Store resubmission are ever needed.

Pace and order live at the top of `generate.py`: `DURATION_MS` (one global equal-time
duration for every piece) and `MODE` (`sequence` or `shuffle`).

Source is public, all rights reserved. Copyright Queueue Studios LLC.
