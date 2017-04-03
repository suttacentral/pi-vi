import pathlib,polib, re

files = list(pathlib.Path('../pt').glob('*/*.po'))


for file in files:
    with file.open('r') as f:
        data = f.read()
    new_data = re.sub(r'(msgctxt ".*"\n)msgctxt', r'\1msgid', data)
    if data != new_data:
        with file.open('w') as f:
            f.write(new_data)

# remove translations

for f in files:
    po = polib.pofile(str(f))
    for entry in po:
        entry.msgstr = ""
    po.save()

# rewrite to one line

for file in files:
    with file.open('r', encoding='utf8') as f:
        data = f.read()
    new_data = re.sub(r'(msgid ""\n(".*?"\n)+)', lambda m: m.groups()[0].replace('"\n"', ''), data)
    if data != new_data:
        with file.open('w', encoding='utf8') as f:
            f.write(new_data)
