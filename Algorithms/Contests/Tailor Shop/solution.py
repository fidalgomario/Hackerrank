#!/bin/python3

import sys

if __name__ == '__main__':
    n,p = input().strip().split(' ')
    n,p = [int(n),int(p)]
    a = [int(i) for i in input().strip().split(' ')]
    a = sorted(a)
    buttons = []
    
    for i in range(len(a)):
        if((a[i] % p != 0) or (a[i] < p)):
            a[i] = a[i] + (p - a[i] % p)
        
        if((i != 0) and (a[i] <= a[i-1])):
            a[i] = a[i-1]+p
        
        buttons.append(a[i]//p)
        
    print(sum(buttons))
