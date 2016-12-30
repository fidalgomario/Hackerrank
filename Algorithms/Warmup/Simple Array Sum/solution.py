#!/bin/python3

import sys

if __name__ == '__main__':

    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    print(sum(arr))
