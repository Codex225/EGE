f = open("26_4604.txt")
n = int(f.readline())
data = [int(x) for x in f]
data.sort(reverse=True)

boxes = [data[0]]
for x in data[1:]:

    if boxes[-1] - x >= 3:

        boxes.append(x)
print(len(boxes), min(boxes))