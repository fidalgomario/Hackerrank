#!/bin/python3

import sys
import itertools

def luckyEight(num):
    arr = [1] + [0] * (8 - 1)
    idx = [[x for x in range(8) if (10*x-i)%8 == 0] for i in range(8)]
    
    for digit in num:
        arr = [(arr[i]%((10**9)+7)) + (sum(arr[x] for x in idx[(i - digit) % 8])%((10**9)+7)) for i in range(8)]
        
    return arr[0] - 1

if __name__ == '__main__':
    n = int(input().strip())
    number = map(int, input().strip())
    print(luckyEight(number) % ((10**9)+7))
