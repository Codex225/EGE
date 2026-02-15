data = [int(x) for x in open("demo_17.txt")]

res = []
min2x = min([x for x in data if (9 < x < 100)])

for i in range(len(data) - 1):
    if ((9 < data[i] < 100) + (9 < data[i + 1] < 100) == 1) and (data[i] + data[i + 1]) % min2x == 0:
        res.append(data[i] + data[i + 1])

print(len(res), max(res))
