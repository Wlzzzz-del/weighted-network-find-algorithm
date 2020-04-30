import pandas as pd
import numpy as np
import math
import networkx as nx
from collections import defaultdict
import func_lib as fl
import select_initial_node as sin
# G = nx.read_edgelist('data set/network1.edgelist', nodetype=int, data=(('weight',float),))
# G=nx.read_gml('data set/lesmis.gml')
G=fl.process_karate(nx.karate_club_graph())
for i in range(2,int(math.sqrt(nx.number_of_nodes(G)))):
    Q=set()
    H=set()
    com=sin.select_initial_nodes(G,i)
    # print(com)
    community=defaultdict(set)
    for k in com:
        community[k]=set()
    while(1):
        # print(len(community.keys()))
        for node in nx.nodes(G):
            index={}
            for center in com:
                index[fl.judge_road_to_sim(G,node,center)]=center
            # print(index[max(index.keys())],node)
            if fl.find_com(G,community,node)==0:
                community[index[max(index.keys())]].add(node)
                # print(community)
            elif fl.find_com(G,community,node)==index[max(index.keys())]:
                continue
            else:
                fl.del_node(node,community)
                community[index[max(index.keys())]].add(node)
            if max(index.keys())<fl.count_avg_com(G,community,index[max(index.keys())]):
                H.add(node)
        for node in com:
            community[node].add(node)
        # print(community)
        # print(i,len(community.keys()))
        new_center=fl.update_center(G,community)
        # print(new_center)
        if new_center==community:
            # print(community)
            community=new_center
            break
        else:
            community=new_center
            com=community.keys()
            # print('ok')
        for node in H:
            index={}
            for c in fl.find_vp(G,community,node):
                index[fl.count_uc(G,community,node,c)]=c
                if fl.find_com(G,community,node)==index[max(index.keys())]:
                    # print(index[max(index.keys())],fl.find_com(G,community,node))
                    continue
                else:
                    community[index[max(index.keys())]].add(node)
                    Q.add(node)
    print(i)
    print('H:', H)
    print('community:', community)
    print('Q:',Q)
    print(fl.count_eqk(G,community))


