#!/bin/python3

import sys

def sumdigits(n):
    return sum(map(int, list(str(n))))

if __name__ == '__main__':
    n = int(input().strip())
    best = 1
    best_sum = 1
    for k in range(1, n + 1):
        if n % k == 0:
            the_sum = sumdigits(k)

            if the_sum > best_sum:
                best_sum = the_sum
                best = k
    print(best)            
