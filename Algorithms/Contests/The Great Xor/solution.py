#!/bin/python3

import sys

def findXor(n):
    binary = "{0:b}".format(n)
    count = 0
    for i in range(0,len(binary)):
        if(binary[i] == '0'):
            count += 2**(len(binary) - 1 - i)
    print(count)

q = int(input().strip())
for a in range(q):
    x = int(input().strip())
    findXor(x)
