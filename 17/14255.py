d = [int(x) for x in open("17_14255.txt")]
resp = []
for x in d:
    if x % 2 != 0:
        resp.append(x)
sr = sum(resp)/len(resp)
print(sr)
res = []
for i in range(1, len(d)):

    if abs(d[i]) % 100 == 11 and  abs(d[i - 1]) % 100 != 11 or abs(d[i]) % 100 != 11 and  abs(d[i - 1]) % 100 == 11:
        if d[i] + d[i-1] >= sr:
            res.append(d[i] + d[i-1])
            #print(res)
print(len(res), max(res))