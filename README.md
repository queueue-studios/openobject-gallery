# OpenObject Gallery

The public sample Host behind **https://gallery.openobject.io**, served as a static
site on GitHub Pages. The OpenObject apps (Apple TV, iPad, iPhone) offer it in the
Host picker's empty state (when no Host is found on the network), so a new owner, or
an App Store reviewer, can see real art immediately without running a Host of their own.

An OpenObject display is a dumb client: it fetches `/api/display` and then the media
that response names. This repo just serves those two things statically:

- `api/display` — a one-item rotation (JSON), matching the player's `/api/display` shape.
- `openobject-gallery-image.jpg` — the artwork the rotation points at (`src`). The name
  is deliberately generic (not the name of any one piece) so the art can be swapped over
  time without changing anything else.
- `CNAME` — binds the site to `gallery.openobject.io`.
- `.nojekyll` — serve files as-is (no Jekyll processing).
- `index.html` — a plain landing page for anyone who opens the domain in a browser.

## Changing the art

Replace `openobject-gallery-image.jpg` with a new JPEG of the same name and commit —
nothing else changes, and the apps keep working. If you switch to a different format
(e.g. PNG), also update `src`, `format`, and `kind` in `api/display` (and the file
extension). To show more than one piece, add items to the `items` array.

Source is public, all rights reserved. Copyright Queueue Studios LLC.
