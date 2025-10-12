from functools import *


#import sys
#sys.setrecursionlimit(10**6)

@lru_cache(None)

def F(n):
    if n == 1: return 1
    else: return n * F(n - 1)


print((F(2024) - F(2023))//F(2022))
