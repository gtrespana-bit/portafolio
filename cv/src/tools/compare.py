"""Compara el texto de dos PDF línea a línea: línea base (dy), x inicial (dx) y anchura (dw), en px CSS.
uso: compare.py original.pdf nuevo.pdf [--all]
Sirve para comprobar que el generador reproduce el diseño del CV original (ver reference/content.original.mjs)."""
import sys, warnings, collections
warnings.filterwarnings('ignore')
import pymupdf
K = 0.75

def text_lines(page):
    out = []
    for b in page.get_text('rawdict', flags=pymupdf.TEXT_PRESERVE_WHITESPACE)['blocks']:
        if b['type'] != 0: continue
        for l in b['lines']:
            chars = []
            for s in l['spans']:
                if 'Type3' in s['font'] or not s['font']: continue      # emoji del original
                for c in s['chars']:
                    chars.append((c, s))
            while chars and not chars[0][0]['c'].strip(): chars.pop(0)
            while chars and not chars[-1][0]['c'].strip(): chars.pop()
            if not chars: continue
            c0, s0 = chars[0]
            txt = ''.join(c['c'] for c, _ in chars)
            if txt in ('▸',): continue
            out.append(dict(text=txt, x0=c0['origin'][0] / K, x1=chars[-1][0]['bbox'][2] / K, base=c0['origin'][1] / K,
                            size=round(s0['size'] / K, 2), font=s0['font'].split('+')[-1], color='#%06x' % s0['color']))
    out.sort(key=lambda r: (round(r['base']), r['x0']))
    return out

def klass(r, pno):
    f = r['font'].lower(); w = 'B' if 'bold' in f and 'semi' not in f else ('S' if 'semibold' in f else 'R')
    s = r['size']; side = r['x0'] < 264
    key = (side, round(s, 1), w)
    table = {(True, 15.3, 'B'): 's-name', (True, 10.0, 'R'): 's-text', (True, 10.0, 'B'): 's-h', (True, 8.7, 'S'): 'sk-label', (True, 8.7, 'R'): 'sk-tag',
             (False, 13.3, 'B'): 'h2', (False, 10.7, 'R'): 'profile', (False, 11.3, 'B'): 'exp-role', (False, 10.0, 'S'): 'exp-co', (False, 9.3, 'R'): 'bullet',
             (False, 8.0, 'S'): 'tag', (False, 9.3, 'B'): 'ach-t', (False, 8.0, 'R'): 'ach-d', (False, 8.7, 'S'): 'edu-d'}
    if key in table: return table[key]
    if key == (False, 8.7, 'R'): return 'exp-date' if r['color'] == '#718096' else 'proj-d'
    if key == (False, 10.0, 'B'): return 'edu-t' if abs(r['x0'] - 298.58) < 1 else 'proj-t'
    return 'otro %s' % (key,)

def main():
    a, b = pymupdf.open(sys.argv[1]), pymupdf.open(sys.argv[2]); show_all = '--all' in sys.argv
    stats = collections.defaultdict(list); rows = []; unmatched = []
    for pno in range(min(a.page_count, b.page_count)):
        la, lb = text_lines(a[pno]), text_lines(b[pno])
        pool = collections.defaultdict(list)
        for r in lb: pool[r['text']].append(r)
        for r in la:
            if pool[r['text']]:
                q = pool[r['text']].pop(0); k = klass(r, pno)
                d = (q['base'] - r['base'], q['x0'] - r['x0'], (q['x1'] - q['x0']) - (r['x1'] - r['x0']), len(r['text']))
                stats[k].append(d); rows.append((pno + 1, k, d, r))
            else: unmatched.append(('solo en el original', pno + 1, r))
        for t, rest in pool.items():
            for q in rest: unmatched.append(('solo en el nuevo', pno + 1, q))
    print('%-9s %4s  %-22s %-16s %-22s %s' % ('clase', 'n', 'dy (media min max)', 'dx (media max)', 'dw (media min max)', 'dw por carácter'))
    for k in sorted(stats):
        v = stats[k]; dy = [x[0] for x in v]; dx = [x[1] for x in v]; dw = [x[2] for x in v]
        per = sum(x[2] for x in v) / max(1, sum(x[3] - 1 for x in v))
        print('%-9s %4d  %+6.2f %+5.1f %+5.1f     %+6.2f %+6.2f    %+6.2f %+6.2f %+6.2f    %+.3f' % (k, len(v), sum(dy) / len(dy), min(dy), max(dy), sum(dx) / len(dx), max(dx, key=abs), sum(dw) / len(dw), min(dw), max(dw), per))
    hist = collections.Counter(round(x[2][0]) for x in rows)
    print('dy (redondeado): ' + '  '.join('%+d px x%d' % (k, hist[k]) for k in sorted(hist)))
    if unmatched:
        print('\nLÍNEAS SIN PAREJA (el texto parte distinto o falta):')
        for why, p, r in unmatched: print('  %-19s p%d y=%7.2f x=%7.2f | %s' % (why, p, r['base'], r['x0'], r['text'][:80]))
    if show_all:
        print()
        for p, k, d, r in rows: print('  p%d %-9s dy %+5.2f dx %+6.2f dw %+6.2f | y=%7.2f | %s' % (p, k, d[0], d[1], d[2], r['base'], r['text'][:60]))

if __name__ == '__main__': main()
