from fontTools.ttLib import TTFont
f = TTFont('x.ttf')
f.flavor = 'woff2'
f.save('x.woff2')
