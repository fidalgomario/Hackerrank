if __name__ == '__main__':
  t = int(input().strip())
  for x in range(t):
      print(~int(input().strip()) & 0xffffffff)
