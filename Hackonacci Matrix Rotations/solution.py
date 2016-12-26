#!/bin/python3

import sys


def changesCount(matrix, degree):
    count = 0
    if(degree == 90):
        for x in range(len(matrix)):
            for i in range(len(matrix)):
                if(matrix[x][i] != matrix[len(matrix) - 1 - i][x]):
                    count += 1
    elif(degree == 180):
        for x in range(len(matrix)):
            for i in range(len(matrix)):
                if(matrix[x][i] != matrix[len(matrix) - 1 - x][len(matrix) - 1 - i]):
                    count += 1
    elif(degree == 270):
        for x in range(len(matrix)):
            for i in range(len(matrix)):
                if(matrix[x][i] != matrix[i][len(matrix) - 1 - x]):
                    count += 1
    
    return count
    
if __name__ == '__main__':
    n,q = input().strip().split(' ')
    n,q = [int(n),int(q)]
    matrix = [[] for x in range(n)]
    counts = [[-1] for x in range(3)]
    
    for i in range(0,n):
        for x in range(0,n):
            num = ((i+1)*(x+1))**2
            num = num % 7 
            if(num == 2 or num == 4 or num == 5):
                matrix[i].append('X')
            else:
                matrix[i].append('Y')

    for a in range(q):
        angle = int(input().strip())
        degree = angle%360
        
        if(degree == 90 and counts[0][0] == -1):
            counts[0][0] = changesCount(matrix, degree)
            print(counts[0][0])
        elif(degree == 90 and counts[0][0] != -1):
            print(counts[0][0])
            
        if(degree == 180 and counts[1][0] == -1):
            counts[1][0] = changesCount(matrix, degree)
            print(counts[1][0])
        elif(degree == 180 and counts[1][0] != -1):
            print(counts[1][0])
            
        if(degree == 270 and counts[2][0] == -1):
            counts[2][0] = changesCount(matrix, degree)
            print(counts[2][0])
        elif(degree == 270 and counts[2][0] != -1):
            print(counts[2][0])
            
        if(degree == 0):
            print(0)
            
