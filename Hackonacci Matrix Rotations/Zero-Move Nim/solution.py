from functools import reduce
from operator import xor

def grundy(x):
    if x % 2:
        return x + 1
    return x - 1
        
g = int(input())

for a in range(g):
    n = int(input())
    grundys = [grundy(int(x)) for x in input().split()]
    if(reduce(xor,grundys)):
        print("W")
    else:
        print("L")
