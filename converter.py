import os

lines = []
with open('fortunes.txt','r') as f:
    for l in f.readlines():
        lines.append(l)

with open('one_liners.py','w') as o:
    o.write('one_liners = [\n')
    for l in lines:
        o.write("r'''"+l.strip()+"''',\n")
    o.write(']')
