from pathlib import Path
import json
p=Path(__file__).parent
data=(p/'data.json').read_text(encoding='utf-8').replace('<','\\u003c')
html=(p/'page.html').read_text(encoding='utf-8').replace('__CSS__',(p/'style.css').read_text(encoding='utf-8')).replace('__DATA__',data).replace('__JS__',(p/'app.js').read_text(encoding='utf-8'))
(p/'index.html').write_text(html,encoding='utf-8')
assert '__CSS__' not in html and '__DATA__' not in html and '__JS__' not in html
print(f'Built {len(html):,} characters, self-contained HTML')
