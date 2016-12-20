#!/bin/python3
import sys
import collections

def connected_components(edges):
    adj = collections.defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    sizes = []
    visited = set()
    for i in adj.keys():
        if i in visited:
            continue
        s = 0
        a = {i}
        while a:
            v = a.pop()
            visited.add(v)
            s += 1
            a.update(adj[v] - visited)
        sizes.append(s)
    return sizes
    
if __name__ == '__main__':
    q = int(input().strip())
    for i in range(q):
        cities,roads,lC,rC = input().strip().split(' ')
        cities,roads,lC,rC = [int(cities),int(roads),int(lC),int(rC)]
        routes = []
        for x in range(roads):
            city_1,city_2 = input().strip().split(' ')
            city_1,city_2 = [int(city_1),int(city_2)]
            routes.append([city_1,city_2])
            
        graph = connected_components(routes)
        res1 = cities*lC    
        res2 = 0
        cityCount = 0
        
        for x in range(len(graph)):
            if(graph[x] > 0):
                res2 += ((graph[x]-1)*rC)+lC
                cityCount += graph[x]
        
        res2 += lC*(cities - cityCount)
        print(min(res1,res2))
