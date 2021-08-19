#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    
    dranked = list(dict.fromkeys(ranked))
    
    p_pos = 0
    d_pos = len(dranked) - 1
    results = []
    while p_pos != len(player):

        if player[p_pos] < dranked[d_pos]:
            results.append(d_pos + 2)
            
        elif player[p_pos] == dranked[d_pos]:
            
            results.append(d_pos + 1)
        
        elif d_pos < 0:
            results.append(1)
            
        else:
            d_pos -= 1
            continue
        
        p_pos += 1
                    
           
    return results
        
    
        
    
if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
