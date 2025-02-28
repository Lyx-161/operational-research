#!/user/bin/env python
# -*- coding:utf -8 -*-
import gurobipy as gp
from gurobipy import GRB

def shortest_path_lp(graph, start, end):
    # create model
    model = gp.Model()
    model.Params.LogToConsole = 0
    #model.Params.LogFile = "gurobi_log.txt"  # 将日志输出到文件
    
    if start == end:
        return 0
    # create various
    x = {}
    for u in graph:
        for v in graph[u]:
            x[u, v] = model.addVar(vtype=GRB.BINARY, name=f'x_{u}_{v}')

    #target function
    model.setObjective(gp.quicksum(graph[u][v]['weight'] * x[u, v] for u in graph for v in graph[u]), GRB.MINIMIZE)

    #s.t.
    for u in graph:
        if u == start:
            model.addConstr(gp.quicksum(x[u, v] for v in graph[u]) == 1, name=f'start_{u}')
        elif u == end:
            model.addConstr(gp.quicksum(x[v, u] for v in graph if (v, u) in x) == 1, name=f'end_{u}')
        else:
            model.addConstr(gp.quicksum(x[v, u] for v in graph if (v, u) in x) == gp.quicksum(x[u, v] for v in graph[u]), name=f'flow_{u}')

    # solver
    model.optimize()

    # print
    if model.status == GRB.OPTIMAL:
        return model.ObjVal
        #print("最短路径:")
        #for u in graph:
        #    for v in graph[u]:
        #        if x[u, v].X > 0.5:
        #            print(f"{u} -> {v} (weight: {graph[u][v]['weight']})")
        print(f"{end}: {int(model.objVal)}",end=', ')
    else:
        print("not found")

