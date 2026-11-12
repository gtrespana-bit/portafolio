"""Vuelca texto, formas e imágenes de un PDF en píxeles CSS (1 px = 0,75 pt).
uso: dump.py archivo.pdf text|shapes|images [página] [xmin xmax]"""
import sys, warnings
warnings.filterwarnings('ignore')
import pymupdf
K = 0.75
def hexc(c):
    if c is None: return '-'
    if isinstance(c, int): return '#%06x' % c
    return '#%02x%02x%02x' % tuple(round(v * 255) for v in c[:3])
def lines(page):
    out = []
    for b in page.get_text('dict', flags=pymupdf.TEXT_PRESERVE_WHITESPACE)['blocks']:
        if b['type'] != 0: continue
        for l in b['lines']:
            sp = [s for s in l['spans'] if s['text'].strip()]
            if not sp: continue
            txt = ''.join(s['text'] for s in l['spans'])
            x0 = min(s['bbox'][0] for s in sp); x1 = max(s['bbox'][2] for s in sp)
            s0 = sp[0]
            out.append(dict(x0=x0 / K, x1=x1 / K, base=s0['origin'][1] / K, size=s0['size'] / K, font=s0['font'], color=hexc(s0['color']), text=txt.strip(), ox=s0['origin'][0] / K))
    out.sort(key=lambda r: (round(r['base']), r['x0']))
    return out
if __name__ == '__main__':
    doc = pymupdf.open(sys.argv[1]); what = sys.argv[2]
    pages = [int(sys.argv[3]) - 1] if len(sys.argv) > 3 else range(doc.page_count)
    xmin = float(sys.argv[4]) if len(sys.argv) > 4 else -1; xmax = float(sys.argv[5]) if len(sys.argv) > 5 else 1e9
    for pno in pages:
        page = doc[pno]
        print('== page %d  %.2f x %.2f px' % (pno + 1, page.rect.width / K, page.rect.height / K))
        if what == 'text':
            for r in lines(page):
                if not (xmin <= r['x0'] <= xmax): continue
                f = r['font'].split('+')[-1].replace('SegoeUI', 'S').replace('Selawik', 'S').replace('-', '')
                print('%7.2f %7.2f %7.2f %5.2f %-10s %s | %s' % (r['base'], r['x0'], r['x1'], r['size'], f[:10], r['color'], r['text'][:70]))
        elif what == 'shapes':
            for d in page.get_drawings():
                r = d['rect']
                if not (xmin <= r.x0 / K <= xmax): continue
                kinds = ''.join(sorted(set(i[0] for i in d['items'])))
                print('%7.2f %7.2f %7.2f %7.2f  w=%6.2f h=%6.2f  %-2s fill=%s a=%s stroke=%s lw=%s n=%d %s' % (r.x0 / K, r.y0 / K, r.x1 / K, r.y1 / K, r.width / K, r.height / K, d['type'], hexc(d.get('fill')), d.get('fill_opacity'), hexc(d.get('color')), ('%.2f' % (d['width'] / K)) if d.get('width') else '-', len(d['items']), kinds))
        elif what == 'images':
            for im in page.get_image_info(xrefs=True):
                b = im['bbox']
                print('%7.2f %7.2f %7.2f %7.2f  w=%6.2f h=%6.2f  %dx%d xref=%d' % (b[0] / K, b[1] / K, b[2] / K, b[3] / K, (b[2] - b[0]) / K, (b[3] - b[1]) / K, im['width'], im['height'], im['xref']))
