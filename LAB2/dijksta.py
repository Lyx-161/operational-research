#!/user/bin/env python
# -*- coding:utf -8 -*-
import heapq
import math

def dijksta(graph,start):
    queue=[]
    heapq.heappush(queue,(0,start)) #distance node

    distances = {node:math.inf for node in graph}
    distances[start] = 0

    while queue:
        current_distance,current_node=heapq.heappop(queue)

        #if current_distance>known_distance skip
        if current_distance>distances[current_node]:
            continue
        #print(current_node,graph[current_node])
        for neighbor,value in graph[current_node].items():
            weight=value['weight']
            #print(graph[current_node].items())
            distance=current_distance+weight

            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(queue,(distance,neighbor))
    return distances
