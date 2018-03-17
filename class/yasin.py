# <dd>Телефон:<br>11114</dd>
# <dd>Телефон:<br>+7 (495) 628 80 03<br>+7 (495) 771 32 23</dd>

import re

with open('kuz.htm', encoding='utf-8') as f:
    html = f.read()

m = re.search(
    r'<dd>Телефон:<br>(.*?)</dd>',
    html)
if m:
    print(m.group())
    print('\n')
    tel = m.groups()[0].split('<br>')
    print('Телефоны: ' + ', '.join(tel))
else:
    print('Телефон не найден')

# ? после *+ уменьшает прожорливость
