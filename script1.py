import sys

velikans = set()

for i in sys.stdin.readlines():
    name, items = i.split()[0], i.split()[1:]
    if 'gold' in items and 'silver' in items:
        velikans.add(name)
print('; '.join(velikans))