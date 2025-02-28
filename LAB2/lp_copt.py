#!/user/bin/env python
# -*- coding:utf -8 -*-
import coptpy as cp
import networkx as nx

def shortest_path_lp(graph, start, end):
    # 创建COPT环境和模型
    env = cp.Envr()
    model = env.createModel()

    model.setParam(cp.COPT.Param.Logging, 0)
    
    if start == end:
        print(f"{end}: 0", end=', ')
        return
    
    # 创建变量：每条边的流量是否为1
    x = {}
    for u in graph:
        for v in graph[u]:
            x[u, v] = model.addVar(vtype=cp.COPT.BINARY, name=f'x_{u}_{v}')

    # 目标函数：最小化路径的总权重
    model.setObjective(cp.quicksum(graph[u][v]['weight'] * x[u, v] for u in graph for v in graph[u]), cp.COPT.MINIMIZE)

    # 约束条件
    for u in graph:
        if u == start:
            model.addConstr(cp.quicksum(x[u, v] for v in graph[u]) == 1, name=f'start_{u}')
        elif u == end:
            model.addConstr(cp.quicksum(x[v, u] for v in graph if (v, u) in x) == 1, name=f'end_{u}')
        else:
            model.addConstr(cp.quicksum(x[v, u] for v in graph if (v, u) in x) == cp.quicksum(x[u, v] for v in graph[u]), name=f'flow_{u}')

    # 求解模型
    model.solve()

    # 输出结果
    if model.status == cp.COPT.OPTIMAL:
        path = []
        for u in graph:
            for v in graph[u]:
                if x[u, v].X > 0.5:  # 如果变量的值为1，则这条边被选中
                    path.append((u, v))
        print(f"{end}: {int(model.objVal)}", end=', ')
        # print("路径:", path)
    else:
        print("路径未找到")