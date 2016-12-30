#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    mario = [(i, grid.index('m')) for i, grid in enumerate(grid) if 'm' in grid]
    princess = [(i, grid.index('p')) for i, grid in enumerate(grid) if 'p' in grid]       


    if(mario != princess):
        if(mario[0][0] != princess[0][0]):
            dis = mario[0][0] - princess[0][0]
            if(dis > 0):
                for x in range(abs(dis)):
                    print("UP")
            else:
                for x in range(abs(dis)):
                    print("DOWN") 
                
        if(mario[0][1] != princess[0][1]):
            dis = mario[0][1] - princess[0][1]
            if(dis > 0):
                for x in range(abs(dis)):
                    print("LEFT") 
            else:
                for x in range(abs(dis)):
                    print("RIGHT") 

    
if __name__ == '__main__':    
  m = int(input())
  grid = [] 
  for i in range(0, m): 
      grid.append(input().strip())

  displayPathtoPrincess(m,grid)
