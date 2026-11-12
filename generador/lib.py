# -*- coding: utf-8 -*-
"""Layout helpers for the Fiverr dossier (ReportLab / Platypus)."""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, KeepTogether, Flowable,
                                NextPageTemplate, CondPageBreak)
from reportlab.platypus.tableofcontents import TableOfContents

import os
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts') + os.sep
for name, fn in [
    ('Plex', 'IBMPlexSans_400Regular'), ('Plex-It', 'IBMPlexSans_400Regular_Italic'),
    ('Plex-Md', 'IBMPlexSans_500Medium'), ('Plex-Sb', 'IBMPlexSans_600SemiBold'),
    ('Plex-Bd', 'IBMPlexSans_700Bold'),
    ('PlexC-Md', 'IBMPlexSansCondensed_500Medium'), ('PlexC-Sb', 'IBMPlexSansCondensed_600SemiBold'),
    ('PlexC-Bd', 'IBMPlexSansCondensed_700Bold'),
    ('Mono', 'IBMPlexMono_400Regular'), ('Mono-Md', 'IBMPlexMono_500Medium'),
    ('Mono-Sb', 'IBMPlexMono_600SemiBold'),
]:
    pdfmetrics.registerFont(TTFont(name, F + fn + '.ttf'))
pdfmetrics.registerFontFamily('Plex', normal='Plex', bold='Plex-Sb', italic='Plex-It', boldItalic='Plex-Sb')
pdfmetrics.registerFontFamily('Mono', normal='Mono', bold='Mono-Sb', italic='Mono', boldItalic='Mono-Sb')

# ---- tokens ---------------------------------------------------------------
INK = colors.HexColor('#17212B')
MUTED = colors.HexColor('#5A6570')
RULE = colors.HexColor('#D5DAE0')
NAVY = colors.HexColor('#0F2A43')
GOLD = colors.HexColor('#A06F12')
GOLD_L = colors.HexColor('#D9B869')
PAPER = colors.HexColor('#F6F2E9')
ZEBRA = colors.HexColor('#F6F7F9')
WARN = colors.HexColor('#9A3B1E')
WARN_BG = colors.HexColor('#FBF1EC')
INFO_BG = colors.HexColor('#EEF3F8')

PAGE_W, PAGE_H = A4
ML, MR, MT, MB = 18 * mm, 18 * mm, 22 * mm, 18 * mm
CW = PAGE_W - ML - MR  # content width

# ---- styles ---------------------------------------------------------------
def ps(name, **kw):
    base = dict(fontName='Plex', bulletFontName='Plex', fontSize=9.4, leading=13.6, textColor=INK, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(name, **base)

ST = {
    'body': ps('body', spaceAfter=5),
    'bodyk': ps('bodyk', spaceAfter=5, keepWithNext=1),
    'small': ps('small', fontSize=8.2, leading=11.4, textColor=MUTED, spaceAfter=4),
    'lead': ps('lead', fontSize=11.2, leading=16.2, spaceAfter=8),
    'h1num': ps('h1num', fontName='Mono-Md', fontSize=10, leading=12, textColor=GOLD, spaceAfter=3),
    'h1': ps('h1', fontName='PlexC-Bd', fontSize=25, leading=28, textColor=NAVY, spaceAfter=4),
    'h2': ps('h2', fontName='PlexC-Sb', fontSize=15, leading=18, textColor=NAVY, spaceBefore=12, spaceAfter=5, keepWithNext=1),
    'h3': ps('h3', fontName='Plex-Sb', fontSize=10.2, leading=13.6, textColor=INK, spaceBefore=8, spaceAfter=3, keepWithNext=1),
    'label': ps('label', fontName='Mono-Md', fontSize=7.2, leading=9.6, textColor=MUTED),
    'bullet': ps('bullet', leftIndent=11, bulletIndent=1, spaceAfter=2.2),
    'cell': ps('cell', fontSize=8.3, leading=11.2),
    'cellb': ps('cellb', fontName='Plex-Sb', fontSize=8.3, leading=11.2),
    'cellm': ps('cellm', fontName='Mono', fontSize=7.6, leading=10.6),
    'cellh': ps('cellh', fontName='PlexC-Sb', fontSize=8.2, leading=10.4, textColor=colors.white),
    'celll': ps('celll', fontName='Mono-Md', fontSize=7.0, leading=9.6, textColor=MUTED),
    'paste': ps('paste', fontSize=9.2, leading=13.2, backColor=PAPER, borderPadding=(7, 8, 7, 9),
                leftIndent=9, rightIndent=8, spaceBefore=10, spaceAfter=16),
    'pastet': ps('pastet', fontName='Plex-Sb', fontSize=10.4, leading=14, backColor=PAPER,
                 borderPadding=(7, 8, 7, 9), leftIndent=9, rightIndent=8, spaceBefore=10, spaceAfter=16),
    'toc0': ps('toc0', fontName='Plex-Sb', fontSize=10, leading=14, spaceBefore=7, textColor=NAVY),
    'toc1': ps('toc1', fontSize=8.6, leading=11.8, leftIndent=14, textColor=INK),
}

_amp = re.compile(r'&(?!(?:[a-zA-Z]+|#\d+);)')

def esc(t):
    return _amp.sub('&amp;', t)

def P(text, style='body'):
    return Paragraph(esc(text), ST[style] if isinstance(style, str) else style)

def bullets(items, style='bullet'):
    return [Paragraph(esc(i), ST[style], bulletText='\u2022') for i in items]

def sp(h=6):
    return Spacer(1, h)

class Rule(Flowable):
    def __init__(self, width=None, color=RULE, thickness=0.6, space=6):
        super().__init__()
        self.w, self.color, self.t, self.space = width, color, thickness, space
    def wrap(self, aw, ah):
        self._w = self.w or aw
        return self._w, self.space
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.t)
        self.canv.line(0, self.space / 2, self._w, self.space / 2)

class H1(Paragraph):
    """Section title. Registers in the TOC and sets the running header."""
    def __init__(self, num, title):
        super().__init__(esc(title), ST['h1'])
        self.num, self.title = num, title

class H2(Paragraph):
    def __init__(self, title, toc=True, tag=None):
        txt = esc(title)
        if tag:
            txt = '<font name="Mono-Md" size="8.5" color="#A06F12">%s</font>&nbsp;&nbsp;%s' % (tag, txt)
        super().__init__(txt, ST['h2'])
        self.title, self.toc, self.tag = title, toc, tag

def section(num, title, intro=None):
    out = [PageBreak(), P(num, 'h1num'), H1(num, title), Rule(color=NAVY, thickness=1.2, space=10)]
    if intro:
        out.append(P(intro, 'lead'))
    return out

def h2(title, toc=True, tag=None):
    return [CondPageBreak(42 * mm), H2(title, toc, tag)]

def h3(title):
    return P(title, 'h3')

def _cell(v, style):
    if isinstance(v, (Flowable, list)):
        return v
    return Paragraph(esc(str(v)), ST[style])

def table(rows, widths, header=True, first_bold=False, mono_cols=(), zebra=True, font=None, repeat=1):
    """rows: list of lists of str. widths: fractions of content width."""
    tot = float(sum(widths))
    cw = [CW * w / tot for w in widths]
    data = []
    for ri, r in enumerate(rows):
        line = []
        for ci, v in enumerate(r):
            if header and ri == 0:
                stl = 'cellh'
            elif ci in mono_cols:
                stl = 'cellm'
            elif first_bold and ci == 0:
                stl = 'cellb'
            else:
                stl = font or 'cell'
            line.append(_cell(v, stl))
        data.append(line)
    t = Table(data, colWidths=cw, repeatRows=repeat if header else 0)
    style = [
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4), ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, RULE),
    ]
    if header:
        style += [('BACKGROUND', (0, 0), (-1, 0), NAVY), ('LINEBELOW', (0, 0), (-1, 0), 0, NAVY),
                  ('TOPPADDING', (0, 0), (-1, 0), 5), ('BOTTOMPADDING', (0, 0), (-1, 0), 5)]
    if zebra:
        start = 1 if header else 0
        for i in range(start, len(rows)):
            if (i - start) % 2 == 1:
                style.append(('BACKGROUND', (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(style))
    t.spaceBefore, t.spaceAfter = 4, 9
    if len(rows) <= 8:
        return KeepTogether([t])
    # no orphaned fragments: keep header + 2 rows, and the last 3 rows, together
    t.setStyle(TableStyle([('NOSPLIT', (0, 0), (-1, 2)), ('NOSPLIT', (0, -3), (-1, -1))]))
    return t

def kv(pairs, w=(22, 78)):
    """Label / value table without header."""
    tot = float(sum(w))
    cw = [CW * x / tot for x in w]
    data = [[Paragraph(esc(k.upper()), ST['celll']), _cell(v, 'cell')] for k, v in pairs]
    t = Table(data, colWidths=cw)
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, -1), 0), ('LEFTPADDING', (1, 0), (1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5), ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LINEBELOW', (0, 0), (-1, -1), 0.4, RULE), ('LINEABOVE', (0, 0), (-1, 0), 0.4, RULE),
    ]))
    t.spaceBefore, t.spaceAfter = 3, 8
    return t

def plain_len(text):
    t = re.sub(r'<br\s*/?>', '\n', text)
    t = re.sub(r'<[^>]+>', '', t)
    t = t.replace('&amp;', '&').replace('&nbsp;', ' ')
    return len(t)

class PasteLabel(Flowable):
    """Label row above a paste block: 'COPIAR  ·  TITLE (EN)' left, counter right."""
    def __init__(self, label, count=None, limit=None):
        super().__init__()
        self.label, self.count, self.limit = label, count, limit
    def wrap(self, aw, ah):
        self._w = aw
        return aw, 11
    def draw(self):
        c = self.canv
        c.setFillColor(GOLD)
        c.rect(0, 1.5, 3, 7.5, stroke=0, fill=1)
        c.setFont('Mono-Md', 7.2)
        c.setFillColor(MUTED)
        c.drawString(8, 2.6, self.label.upper())
        if self.count is not None:
            over = self.limit and self.count > self.limit
            c.setFillColor(WARN if over else MUTED)
            txt = ('%d / %d caracteres' % (self.count, self.limit)) if self.limit else '%d caracteres' % self.count
            c.drawRightString(self._w, 2.6, txt)

def paste(label, text, limit=None, title=False):
    """Copy-ready block. text uses \n for line breaks."""
    html = esc(text).replace('\n', '<br/>')
    n = plain_len(html)
    if limit and n > limit:
        raise ValueError('Paste block over limit (%d > %d): %s' % (n, limit, label))
    par = Paragraph(html, ST['pastet' if title else 'paste'])
    head = PasteLabel(label, n, limit)
    if n < 500:
        return [KeepTogether([head, par])]
    return [CondPageBreak(30 * mm), head, par]

def note(text, kind='info', title=None):
    bg, bar = (WARN_BG, WARN) if kind == 'warn' else (INFO_BG, NAVY)
    body = []
    if title:
        body.append(Paragraph(esc(title), ps('nt', fontName='Plex-Sb', fontSize=9.2, leading=12.6,
                                               textColor=bar, spaceAfter=2)))
    for t in (text if isinstance(text, list) else [text]):
        body.append(Paragraph(esc(t), ps('nb', fontSize=8.9, leading=12.6, spaceAfter=2)))
    t = Table([[body]], colWidths=[CW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg), ('LINEBEFORE', (0, 0), (0, -1), 2.2, bar),
        ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 7), ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    t.spaceBefore, t.spaceAfter = 5, 10
    return t

def stats(items, cols=4, dark=False):
    """items: list of (number, label)."""
    num = ps('sn', fontName='Mono-Sb', fontSize=17, leading=20, textColor=colors.white if dark else NAVY)
    lab = ps('sl', fontSize=7.9, leading=10.4, textColor=colors.HexColor('#B9C6D3') if dark else MUTED)
    rows, row = [], []
    for n, l in items:
        row.append([Paragraph(esc(n), num), Paragraph(esc(l), lab)])
        if len(row) == cols:
            rows.append(row); row = []
    if row:
        row += [''] * (cols - len(row)); rows.append(row)
    t = Table(rows, colWidths=[CW / cols] * cols)
    line = colors.HexColor('#2C4660') if dark else RULE
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'), ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8), ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 9), ('LINEABOVE', (0, 0), (-1, -1), 0.6, line),
    ]))
    t.spaceBefore, t.spaceAfter = 6, 10
    return t

# ---- document -------------------------------------------------------------
class Doc(BaseDocTemplate):
    def __init__(self, path, **kw):
        super().__init__(path, pagesize=A4, leftMargin=ML, rightMargin=MR, topMargin=MT, bottomMargin=MB, **kw)
        self.section = ''
        frame = Frame(ML, MB, CW, PAGE_H - MT - MB, id='f', leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
        cover = Frame(ML, MB, CW, PAGE_H - 2 * MB, id='c', leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id='cover', frames=[cover], onPage=self._cover_bg),
            PageTemplate(id='main', frames=[frame], onPageEnd=self._chrome),
        ])

    def beforeDocument(self):
        self.section = 'Contenido'

    def _cover_bg(self, c, doc):
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
        c.restoreState()

    def _chrome(self, c, doc):
        c.saveState()
        c.setFont('Mono', 7)
        c.setFillColor(MUTED)
        y = PAGE_H - 13 * mm
        c.drawString(ML, y, 'DOSSIER FIVERR  \u00b7  GTRESPANA-BIT')
        c.drawRightString(PAGE_W - MR, y, (self.section or '').upper())
        c.setStrokeColor(RULE); c.setLineWidth(0.5)
        c.line(ML, y - 4, PAGE_W - MR, y - 4)
        c.drawRightString(PAGE_W - MR, 10 * mm, '%d' % doc.page)
        c.drawString(ML, 10 * mm, '11 NOV 2026')
        c.restoreState()

    def afterFlowable(self, fl):
        if isinstance(fl, H1):
            self.section = fl.title
            key = 's%s' % re.sub(r'\W', '', fl.num)
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry('%s  %s' % (fl.num, fl.title), key, 0)
            self.notify('TOCEntry', (0, '%s  %s' % (fl.num, fl.title), self.page, key))
        elif isinstance(fl, H2) and fl.toc:
            key = 'h%d' % id(fl)
            self.canv.bookmarkPage(key)
            label = ('%s  %s' % (fl.tag, fl.title)) if fl.tag else fl.title
            self.canv.addOutlineEntry(label, key, 1)
            self.notify('TOCEntry', (1, label, self.page, key))

def toc():
    t = TableOfContents()
    t.levelStyles = [ST['toc0'], ST['toc1']]
    t.dotsMinLevel = 1
    return t
