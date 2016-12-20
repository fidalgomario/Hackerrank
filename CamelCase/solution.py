#!/bin/python3

import sys
if __name__ == '__main__':
  word = input()

  count = 1

  for letter in word:
      if(str(letter).isupper()):
          count += 1

  print (count)
