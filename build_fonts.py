#!/usr/bin/env python3

from fontTools.ttLib import TTFont

GIT_USER = "izuk"
GIT_PROJECT = "agda-fonts"
BASE_URL = "https://cdn.jsdelivr.net/gh"

FONTS_SRC = "fonts/src"
FONTS_BUILD = "fonts/build"

FONTS_CONFIG = {
  "DejaVuSansMono": [
    {
      "src": "DejaVu Sans Mono Bold for Powerline",
      "font-weight": "bold",
      "font-style": "normal",
    },
    {
      "src": "DejaVu Sans Mono Bold Oblique for Powerline",
      "font-weight": "bold",
      "font-style": "oblique",
    },
    {
      "src": "DejaVu Sans Mono for Powerline",
      "font-weight": "normal",
      "font-style": "normal",
    },
    {
      "src": "DejaVu Sans Mono Oblique for Powerline",
      "font-weight": "normal",
      "font-style": "oblique",
    },
  ],
}

css = []
for path, confs in FONTS_CONFIG.items():
  for conf in confs:
    font = TTFont("%s/%s/%s.ttf" % (FONTS_SRC, path, conf["src"]))
    font.flavor = "woff2"
    font.save("%s/%s/%s.woff2" % (FONTS_BUILD, path, conf["src"]))
    css += [
      "@font-face {",
      "  font-family: \"%s\";" % path,
      "  src: url(\"%s/%s.woff2\") format(\"woff2\");" % (path, conf["src"]),
      "  font-weight: %s;" % conf["font-weight"],
      "  font-style: %s;" % conf["font-style"],
      "}",
    ]

css = filter(None, css)

with open("%s/fonts.css" % FONTS_BUILD, "w") as f:
    f.write("\n".join(css))

print("%s/%s/%s@master/%s/fonts.css" % (BASE_URL, GIT_USER, GIT_PROJECT, FONTS_BUILD))
