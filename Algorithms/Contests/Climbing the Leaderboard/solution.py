#!/bin/python3

import sys
import bisect

if __name__ == '__main__':
  n = int(input().strip())
  scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
  m = int(input().strip())
  alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
  scoreSet = sorted(set(scores))

  size = len(scoreSet)

  for i in range(m):
      index = bisect.bisect_left(scoreSet, alice[i])

      if((index != size) and (alice[i] == scoreSet[index])):
          print(size - index)
      else:
          print(size + 1 - index)
