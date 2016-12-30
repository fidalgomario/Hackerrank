#!/bin/python3

if __name__ == '__main__':
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    arr = [int(a) for a in input().strip().split(' ')]
    
    count = 0
    index = 1
    for i in range(0,len(arr) - 1):
        for x in range(index, len(arr)):
            if((arr[i] + arr[x]) % k == 0):
                count = count + 1
                
        index = index + 1        
    print(count)
