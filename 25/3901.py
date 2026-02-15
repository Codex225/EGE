from fnmatch import *

for i in range(700_000, 700_000 + 250):
    if i % 13 == 0 and not (fnmatch(str(i), "*0??3*") or fnmatch(str(i), "*4??2")\
            or fnmatch(str(i), "*1*")):
        print(i, sum([int(x) for x in str(i)]))