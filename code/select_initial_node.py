import pandas as pd
import numpy as np
import math
import networkx as nx
from collections import defaultdict
import func_lib as fl

def select_initial_nodes(G,K):
    ##load dataset and add weight
    # G=fl.process_karate(nx.karate_club_graph())
    # G=nx.read_gml('data set/lesmis.gml')
    NS={}
    I=[]
    a=2
    #count the Aggregation strength of every node and sort them
    for node in G.nodes():
        NS[node]=fl.Aggre_strength(G,node)

    NS=sorted(NS.items(), key=lambda item:item[1],reverse=True)
    #select max Aggregation strength as first initial node
    I.append(NS[0][0])
    NS.remove(NS[0])
    while(len(I)<K):
        n=NS[0][0]
        for i in I:
            # print(fl.judge_road_to_sim(G,n,i))
            if fl.judge_road_to_sim(G,n,i)>a:
                del NS[0]
                break
        I.append(n)
        del NS[0]
    return I
# G=fl.process_karate(nx.karate_club_graph())
G=nx.read_gml('data set/lesmis.gml')
for i in range(2,int(math.sqrt(nx.number_of_nodes(G)))):
    print(select_initial_nodes(G,i))