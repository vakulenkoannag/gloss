import re

with open('kuz.htm', encoding='utf-8') as f:
    html = f.read()

m = re.search(
    r'<ul>.*?</ul>',
    html,
    re.DOTALL+re.IGNORECASE
)

if m:
    print(m.group())
else:
    print('Ничего не найдено')

# ? после *+ уменьшает прожорливость
