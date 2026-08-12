s = open("24-d3.txt").read().strip()

maxlen = 0
k = 1

for i in range(len(s) - 1):
    if s[i+1] == s[i]:
        k = k + 1
        maxlen = max(maxlen, k)
    else:
        k = 1
print(maxlen)

# for x in 'MNP':
#   for y in 'MNP':
#     if x!=y:
#       s = s.replace(x+y,x+' '+y)
# print(max(map(len,s.split())))