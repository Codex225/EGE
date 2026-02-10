from re import finditer
res = []
f = open("24_4602.txt")
s = f.read().strip()
pat = r"([BCD][AO])+"
reg = rf"(?=({pat}))" #используем для страховки от пересечений
for s1 in finditer(reg, s):
    res.append(len(s1[1]))
print(max(res) // 2)

# from re import finditer
# res = []
# f = open("24_4602.txt")
# s = f.read().strip()
# reg = r"(BA|BO|CA|CO|DA|DO)+"
# #reg = r"([BCD][AO])+"
# for s1 in finditer(reg, s):
#     res.append(len(s1[0]))
# print(max(res))