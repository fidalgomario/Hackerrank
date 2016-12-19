import sys
if __name__ == '__main__':
  n,m = input().strip().split(' ')
  n,m = [int(n),int(m)]

  print(((n+1)//2)*((m+1)//2))
