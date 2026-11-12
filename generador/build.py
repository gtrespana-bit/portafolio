# -*- coding: utf-8 -*-
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lib import Doc
import c1_intro, c2_projects, c3_services, c4_gigs, c5_strategy

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'dossier-fiverr.pdf')

story = []
story += c1_intro.cover()
story += c1_intro.build()
story += c3_services.stack_section()
story += c2_projects.build()
story += c3_services.build()
story += c4_gigs.build()
story += c5_strategy.build()

from reportlab.platypus import Paragraph, Table, KeepTogether
from lib import ST
for i in range(len(story) - 1):
    a, b = story[i], story[i + 1]
    if isinstance(a, Paragraph) and a.style.name == 'body' and isinstance(b, (Table, KeepTogether)):
        a.style = ST['bodyk']
import copy
from lib import H2
h2free = copy.copy(ST['h2']); h2free.keepWithNext = 0
for i in range(len(story) - 1):
    a, b = story[i], story[i + 1]
    # A heading before a long, splittable table must not drag the whole table to the next page.
    if isinstance(a, H2) and isinstance(b, Table):
        a.style = h2free

doc = Doc(OUT, title='Dossier Fiverr: experiencia, servicios y gigs',
          author='gtrespana-bit', subject='Experiencia y cat\u00e1logo de servicios para Fiverr',
          lang='es')
doc.multiBuild(story)
print('ok', OUT, 'services', c3_services.COUNT, 'gigs', len(c4_gigs.GIGS))
