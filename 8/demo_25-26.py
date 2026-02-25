c = 0
s = "акорст"
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    str = i1 + i2 + i3 + i4 + i5
                    c +=1
                    if c % 2 == 0 and str[0] != "а" and str[0] != "с" and str[0] != "а"and str[0] != "т"\
                        and str.count("о") == 2:
                        print(str, c)