#!/bin/python3

import sys

if __name__ == '__main__':
    s,t = input().strip().split(' ') #house position
    s,t = [int(s),int(t)]
    a,b = input().strip().split(' ') #tree positions
    a,b = [int(a),int(b)]
    m,n = input().strip().split(' ') #number of apples and oranges
    m,n = [int(m),int(n)]
    apple = [int(a) for a in input().strip().split(' ')] #apple positions
    orange = [int(o) for o in input().strip().split(' ')] #orange positions
    
    aCount = 0
    oCount = 0
    for x in range(len(apple)):
        if s <= (apple[x] + a) <= t:
            aCount = aCount + 1
            
    for x in range(len(orange)):
        if s <= (orange[x] + b) <= t:
            oCount = oCount + 1
            
    print(aCount)
    print(oCount)
