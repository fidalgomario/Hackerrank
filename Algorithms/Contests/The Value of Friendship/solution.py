#!/bin/python3

import sys
import collections
from collections import defaultdict



def countFriends(num,n):
    res = 0
    for i in range(2,n+1):
        res += (i-1)*(i)
        res += num
    return res
        
def friendships(edges, count):
    
    adj = collections.defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    sizes = []
    visited = set()
    for i in adj.keys():
        if i in visited:
            count += 1
            continue
        s = 0
        a = {i}
        while a:
            v = a.pop()
            visited.add(v)
            s += 1
            a.update(adj[v] - visited)
        sizes.append(s)
    return sizes,count

if __name__ == '__main__':
    t = int(input().strip())
    for a in range(t):
        n,m = input().strip().split(' ')
        n,m = [int(n),int(m)]

        friends = []
        for a1 in range(m):
            x,y = input().strip().split(' ')
            x,y = [int(x),int(y)]
            friends.append([x,y])


        count = 0    
        friendShips, count = friendships(friends,count)  
        friendShips = (sorted(friendShips, reverse=True))

        prev = 0
        total_friends = 0
        dup = m - count 

        for x in friendShips:
            total_friends += countFriends(prev,x)
            prev += (x-1) * (x)

        total_friends += dup * prev
        print(total_friends)
