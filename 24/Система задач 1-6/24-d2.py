s = open("24-d2.txt").read().strip()

maxlen = 0
k = 0
for i in range(len(s)):
    if s[i].isdigit():
        k = k + 1
        maxlen = max(maxlen, k)
    else:
        k = 0
print(maxlen)

for c in set(s):
  if not c.isdigit():
    s = s.replace(c,' ')
print(max(map(len,s.split())))

