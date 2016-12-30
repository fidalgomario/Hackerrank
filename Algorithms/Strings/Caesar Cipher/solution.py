#!/bin/python3

if __name__ == '__main__':
  n = int(input().strip())
  s = input().strip()
  k = int(input().strip())

  alpha = "abcdefghijklmnopqrstuvwxyz"
  ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  res = ""
  for i in range(len(s)):
      if(s[i].isalpha() and s[i].islower()):
          res += alpha[((ord(s[i]) + k - 97) % 26)]
      elif(s[i].isalpha() and s[i].isupper()):
          res += ALPHA[((ord(s[i]) + k - 65) % 26)]
      else:
          res += s[i]

  print(res)
