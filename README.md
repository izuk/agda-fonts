A little tool and repository for Chrome Secure Shell fonts that work well
with Agda.

To use, set this in the "Custom CSS" field:

> https://cdn.jsdelivr.net/gh/izuk/agda-fonts@master/fonts/build/fonts.css

and use this font family:

> DejaVuSansMono

To rebuild the CSS and woff2 files:

```
$ git submodule init
$ nix-shell  # On NixOS.
$ build_fonts.py
```
