#!/bin/python3

import sys


n = int(input().strip())
p = int(input().strip())
pages = []

x = min((p//2),abs((p//2)-(n//2)))
print(x)
