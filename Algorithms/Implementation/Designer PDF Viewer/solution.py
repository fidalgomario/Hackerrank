#!/bin/python3

import sys

if __name__ == '__main__':
    heights = [int(h) for h in input().strip().split(' ')]
    word = input().strip()
    
    letters = []
    for x in word:
        letters.append(heights[ord(x) - ord('a')])
    print(max(letters) * len(word))
