#!/bin/python3

import sys

if __name__ == '__main__':
    n = int(input().strip())
    socks = [int(s) for s in input().strip().split(' ')]

    pairs = {}

    for x in socks:
        if not x in pairs:
            pairs[x] = 1
        else:
            pairs[x] = pairs.get(x) + 1

    count = 0
    for i in pairs:
        count = count + (pairs.get(i) //2)

    print(count)
