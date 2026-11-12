"""Pone el mismo recorte de dos PDF uno al lado del otro (izquierda: primero; derecha: segundo).
uso: sidebyside.py a.pdf b.pdf salida.png zoom página:x0,y0,x1,y1 [página:x0,y0,x1,y1 ...]   (px CSS, página desde 1)"""
import sys, warnings
warnings.filterwarnings('ignore')
import pymupdf
K = 0.75
a, b, out, zoom = pymupdf.open(sys.argv[1]), pymupdf.open(sys.argv[2]), sys.argv[3], float(sys.argv[4])
rows = []
for spec in sys.argv[5:]:
    pno, box = spec.split(':'); x0, y0, x1, y1 = [float(v) for v in box.split(',')]
    clip = pymupdf.Rect(x0 * K, y0 * K, x1 * K, y1 * K); m = pymupdf.Matrix(zoom / K, zoom / K)
    rows.append((a[int(pno) - 1].get_pixmap(matrix=m, clip=clip, alpha=False), b[int(pno) - 1].get_pixmap(matrix=m, clip=clip, alpha=False)))
gap = 12
W = max(l.width + r.width + gap for l, r in rows); H = sum(max(l.height, r.height) for l, r in rows) + gap * (len(rows) - 1)
doc = pymupdf.open(); page = doc.new_page(width=W, height=H)
page.draw_rect(page.rect, color=None, fill=(1, 0, 1))
y = 0
for l, r in rows:
    page.insert_image(pymupdf.Rect(0, y, l.width, y + l.height), pixmap=l)
    page.insert_image(pymupdf.Rect(l.width + gap, y, l.width + gap + r.width, y + r.height), pixmap=r)
    y += max(l.height, r.height) + gap
page.get_pixmap(alpha=False).save(out); print(out, W, H)
