#!/bin/python3

import sys


n,c,m = input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = list(map(int, input().strip().split(' ')))

mostPeople = max(p)
capacity = m*c

if(capacity < mostPeople):
    print("No")
else:
    print("Yes")
