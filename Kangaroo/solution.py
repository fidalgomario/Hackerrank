#!/bin/python3

import sys

#!/bin/python3

import sys

if __name__ == '__main__':
    x1,v1,x2,v2 = input().strip().split(' ')
    x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

    pos1 = x1
    pos2 = x2
    while(True):
        if(pos1 > pos2 and v1 > v2):
            print("NO")
            break
        elif(pos1 < pos2 and v1 < v2):
            print("NO")
            break
        elif(pos1 < pos2 and v1 == v2):
            print("NO")
            break
        else:
            pos1 = pos1 + v1
            pos2 = pos2 + v2

        if(pos1 == pos2):
            print("YES")
            break
