#!/bin/python3

import sys

if __name__ == '__main__':

    a = [int(x) for x in input().strip().split(' ')]
    b = [int(x) for x in input().strip().split(' ')]
    
    alice = 0
    bob = 0
    
    for i in range(len(a)):
        if(a[i] > b[i]):
            alice += 1
        elif(a[i] < b[i]):
            bob += 1
            
    print(alice, bob)
