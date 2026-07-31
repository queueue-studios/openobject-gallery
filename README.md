# OpenObject Gallery

The public sample Host behind **https://gallery.openobject.io**, served as a static
site on GitHub Pages. The OpenObject apps (Apple TV, iPad, iPhone) offer it in the
Host picker's empty state (when no Host is found on the network), so a new owner, or
an App Store reviewer, can see real art immediately without running a Host of their own.

An OpenObject display is a dumb client: it fetches `/api/display` and then the media
that response names. This repo just serves those two things statically:

- `api/display` — the rotation (JSON), matching the player's `/api/display` shape. It
  lists three pieces on an 8-second equal-time rotation, in sequence order, so the
  Gallery shows what OpenObject actually does (a rotating art player) rather than a
  single still.
- `openobject-gallery-1.jpg`, `-2.jpg`, `-3.jpg` — the artwork the rotation cycles
  through. The names are deliberately generic (not the name of any one piece) so the
  art can be swapped over time without changing anything else.
- `CNAME` — binds the site to `gallery.openobject.io`.
- `.nojekyll` — serve files as-is (no Jekyll processing).
- `index.html` — a plain landing page for anyone who opens the domain in a browser.

## Changing the art

Replace any of `openobject-gallery-1/2/3.jpg` with a new JPEG of the same name and
commit — nothing else changes, and the apps keep working. To change how many pieces
rotate, add or remove items in `api/display`'s `items` array (and add/remove the
matching image files). To change the pace, edit `durationMs` (milliseconds, one global
value for all pieces). If you switch a piece to a different format (e.g. PNG), also
update that item's `src`, `format`, and `kind` (and the file extension).

Source is public, all rights reserved. Copyright Queueue Studios LLC.
