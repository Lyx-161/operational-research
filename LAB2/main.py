# -*- coding:utf -8 -*-
import networkx as nx
import random
import time
import numpy as np
import math
import openpyxl

import dijksta
import lp_gurobi as lp
import is_welldefine
#import lp_copt as lp

def generate_G(nodenum,p):
    for i in range(nodenum):
        for j in range(i+1,nodenum,1):
            p_num=random.random()
            if(p_num<p):
                G.add_edge(i,j)
                G.edges[i,j]['weight']=random.randint(1,10)
    return G

if __name__=="__main__":

    '''wb = openpyxl.Workbook()
    ws = wb.active

    ws.title="Sample Sheet"
    ws.append(["node_num","edge_num","time"])

    for i in range(10,10000,10):
        times=np.zeros(10)
        edge=np.zeros(10)
        for j in range(10):

            

        ws.append([nodenum,edge[0],edge[1],edge[2],edge[3],edge[4],edge[5],
                   edge[6],edge[7],edge[8],edge[9],times[0],times[1],times[2],
                   times[3],times[4],times[5],times[6],times[7],times[8],times[9]])

        wb.save("sample.xlsx")

    wb.save("sample.xlsx")'''

    nodenum=100
    p=0.1
    starttime=time.time()
    G=nx.Graph()
    G=generate_G(nodenum,p)
    endtime=time.time()
    print(endtime-starttime)
    start=list(G.nodes)[0]
    if is_welldefine.is_positive(G):

        starttime=time.time()
        distance={}
        for i in G.nodes:
            distance[i]=lp.shortest_path_lp(G, start, i)
        endtime=time.time()
        print(distance,endtime-starttime)
        print(endtime-starttime)


        print(G)
        #print(start)
        starttime=time.time()
        distances=dijksta.dijksta(G,start)
        endtime=time.time()
        if all(distances[node] != math.inf for node in G): 
            print(distances,endtime-starttime)
            print(endtime-starttime)
        else:
            print("is not liantong")


