"""Compara la «tinta» (píxeles distintos del fondo) de iconos, viñetas y puntos entre dos PDF.
uso: inkcmp.py original.pdf nuevo.pdf      (regiones pensadas para reference/content.original.mjs)"""
import sys, warnings
warnings.filterwarnings('ignore')
import pymupdf
K = 0.75

def ink(doc, pno, x0, y0, x1, y1, tol=40, Z=8):
    pm = doc[pno].get_pixmap(matrix=pymupdf.Matrix(Z / K, Z / K), clip=pymupdf.Rect(x0 * K, y0 * K, x1 * K, y1 * K), alpha=False)
    bg = pm.pixel(0, 0); xs = []; ys = []
    for y in range(pm.height):
        for x in range(pm.width):
            c = pm.pixel(x, y)
            if abs(c[0] - bg[0]) + abs(c[1] - bg[1]) + abs(c[2] - bg[2]) > tol: xs.append(x); ys.append(y)
    if not xs: return None
    return (x0 + min(xs) / Z, y0 + min(ys) / Z, x0 + (max(xs) + 1) / Z, y0 + (max(ys) + 1) / Z)

REGIONS = [
    ('emoji correo', 0, 25, 276, 44, 294), ('emoji teléfono', 0, 25, 297, 44, 314), ('emoji chincheta', 0, 25, 334, 44, 351), ('emoji pulpo', 0, 25, 354, 44, 371),
    ('emoji proyecto 1', 1, 309, 80, 325.5, 96), ('emoji proyecto 2', 1, 309, 199, 325.5, 215), ('emoji proyecto 3', 1, 309, 292, 325.5, 308), ('emoji proyecto 4', 1, 309, 399, 325.5, 415),
    ('emoji logro 1', 1, 305, 530, 326, 549), ('emoji logro 2', 1, 539, 530, 560, 549), ('emoji logro 3', 1, 305, 608, 326, 627), ('emoji logro 4', 1, 539, 608, 560, 627),
    ('emoji logro 5', 1, 305, 685, 326, 704), ('emoji logro 6', 1, 539, 685, 560, 704),
    ('viñeta 1', 0, 311, 299, 323, 311), ('viñeta 2', 0, 311, 329, 323, 341), ('viñeta ítem 2', 0, 311, 504, 323, 516),
    ('punto línea de tiempo 1', 0, 288, 246, 298.9, 265), ('punto línea de tiempo 2', 0, 288, 451, 298.9, 470),
    ('punto idioma 1', 0, 187, 951, 197.5, 962), ('punto idioma 5', 0, 229.5, 951, 240, 962), ('punto idioma fila 3, 1', 0, 187, 986, 197.5, 997),
    ('foto (aro)', 0, 70, 30, 195, 158),
]

if __name__ == '__main__':
    a, b = pymupdf.open(sys.argv[1]), pymupdf.open(sys.argv[2])
    print('%-26s %-34s %-34s %s' % ('región', 'original (x0 y0 x1 y1)', 'nuevo', 'diferencia'))
    for name, pno, x0, y0, x1, y1 in REGIONS:
        A, B = ink(a, pno, x0, y0, x1, y1), ink(b, pno, x0, y0, x1, y1)
        f = lambda t: ' '.join('%7.2f' % v for v in t) if t else '-'
        d = ' '.join('%+5.2f' % (q - p) for p, q in zip(A, B)) if A and B else ''
        print('%-26s %-34s %-34s %s' % (name, f(A), f(B), d))
