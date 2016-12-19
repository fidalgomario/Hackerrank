#!/bin/python3

if __name__ == '__main__':
    t = int(input())
    
    for x in range(t):
        n = int(input())
        if(n % 7 > 1):
            print("First")
        else:
            print("Second")
                      
