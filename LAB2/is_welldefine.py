#!/user/bin/env python
# -*- coding:utf -8 -*-
import dijksta

def is_positive(graph):
    for i in graph:
        for j in graph[i]:
            if graph[i][j]['weight']<0:
                print("has negetive edge")
                return False
    return True
