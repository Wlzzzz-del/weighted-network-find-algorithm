import pandas as pd
import numpy as np
import networkx as nx
import math
from collections import defaultdict

'process karate dataset into weights'
def process_karate(G):
    a = pd.read_excel('./karate weighted data.xlsx')
    G.add_weighted_edges_from(a.values.tolist(),weight='value')
    return G

'add value to process the undirect network'
def add_value(G):
    weights=1/G.number_of_edges()
    for i in G.edges():
        G.add_weighted_edges_from([(i[0],i[1],weights)],weight='value')
    return G

'count Aggregation strength'
def Aggre_strength(G,node):
    H=set()
    num_of_edge=0
    for i in G.__getitem__(node):
        num_of_edge=num_of_edge+1
        H.add(i)
        for n in G.__getitem__(i):
            num_of_edge=num_of_edge+1
            H.add(n)
    num_of_nei=len(H)
    p=(num_of_nei*(num_of_nei-1))/2
    if p==0:
        p=1
    return (num_of_edge*num_of_nei)/p

'count connected nodes similarity'
def sim_vi_vj_connect(G,vi,vj):
    sim=0
    sij=0
    a=[]
    b=[]
    w=G[vi][vj]['value']
    for i in G.__getitem__(vi):
        sij=sij+G[vi][i]['value']
    for j in G.__getitem__(vj):
        sij=sij+G[vj][j]['value']
    sim=G[vi][vj]['value']/(sij-w)
    ##first common nei
    for i in G.__getitem__(vi):
        a.append(i)
        for n in G.__getitem__(vj):
            if n in a:
                b.append(n)
    for i in b:
        sim=sim+((G[i][vi]['value']+G[i][vj]['value'])/(sij-w))/len(G.__getitem__(i))
    a=[]
    b={}
    for i in G.__getitem__(vi):
        a.append(i)
        for n in G.__getitem__(vj):
            for k in G.__getitem__(n):
                if k in a:
                    b[k]=n
    for i in list(b):
        sim=sim+((G[i][vi]['value']+G[i][b[i]]['value']*G[vj][b[i]]['value'])/(sij-w))/len(G.__getitem__(i))
    a=[]
    b={}
    for i in G.__getitem__(vj):
        a.append(i)
        for n in G.__getitem__(vi):
            for k in G.__getitem__(n):
                if k in a:
                    b[k]=n
    for i in list(b):
        try:
            # print(1)
            sim=sim+((G[i][vj]['value']+G[i][b[i]]['value']*G[vj][b[i]]['value'])/(sij-w))/len(G.__getitem__(i))
        except:
            # print(0)
            sim=sim
    a={}
    b={}
    c=[]
    for i in G.__getitem__(vi):
        for n in G.__getitem__(i):
            a[n]=i
    for i in G.__getitem__(vj):
        for n in G.__getitem__(i):
            b[n]=i
    for i in list(b):
        if i in list(a):
            c.append(i)
    for i in c:
        sim=sim+(((G[i][a[i]]['value']*G[a[i]][vi]['value'])+(G[i][b[i]]['value']*G[b[i]][vj]['value']))/(sij-w))/len(G.__getitem__(i))
    return sim

'count unconnect nodeds sim'
def sim_vi_vj_unconnet(G,vi,vj):
    sim=0
    sij=0
    a=[]
    b=[]
    for i in G.__getitem__(vi):
        sij=sij+G[vi][i]['value']
    for j in G.__getitem__(vj):
        sij=sij+G[vj][j]['value']
    ##first common nei
    for i in G.__getitem__(vi):
        a.append(i)
        for n in G.__getitem__(vj):
            if n in a:
                b.append(n)
    for i in b:
        sim=sim+((G[i][vi]['value']+G[i][vj]['value'])/(sij))/len(G.__getitem__(i))
    a=[]
    b={}
    for i in G.__getitem__(vi):
        a.append(i)
        for n in G.__getitem__(vj):
            for k in G.__getitem__(n):
                if k in a:
                    b[k]=n
    for i in list(b):
        sim=sim+((G[i][vi]['value']+G[i][b[i]]['value']*G[vj][b[i]]['value'])/(sij))/len(G.__getitem__(i))
    a=[]
    b={}
    for i in G.__getitem__(vj):
        a.append(i)
        for n in G.__getitem__(vi):
            for k in G.__getitem__(n):
                if k in a:
                    b[k]=n
    for i in list(b):
        try:
            # print(1)
            sim=sim+((G[i][vj]['value']+G[i][b[i]]['value']*G[vj][b[i]]['value'])/(sij))/len(G.__getitem__(i))
        except:
            # print(0)
            sim=sim
    a={}
    b={}
    c=[]
    for i in G.__getitem__(vi):
        for n in G.__getitem__(i):
            a[n]=i
    for i in G.__getitem__(vj):
        for n in G.__getitem__(i):
            b[n]=i
    for i in list(b):
        if i in list(a):
            c.append(i)
    for i in c:
        sim=sim+(((G[i][a[i]]['value']*G[a[i]][vi]['value'])+(G[i][b[i]]['value']*G[b[i]][vj]['value']))/(sij))/len(G.__getitem__(i))
    return sim

'judge nodes path then count sim'
def judge_road_to_sim(G,vi,vj):
    a=nx.shortest_path_length(G,source=vi,target=vj)
    if(a==1):
        return sim_vi_vj_connect(G,vi,vj)
    elif(a>4):
        return 0
    else:
        return sim_vi_vj_unconnet(G,vi,vj)

def count_avg_com(G,com,center):
    a=[]
    sim=0
    cj=len(com[center])
    for i in com[center]:
        a.append(i)
        for n in com[center]:
            if n not in a:
                sim=sim+judge_road_to_sim(G,i,n)
    if cj ==1:
        return  (2*sim)/2
    return (2*sim)/(cj*(cj-1))

def update_center(G,com):
    com_new={}
    I={}
    for i in com:
        index={}
        a=[]
        sim=0
        if len(com[i])==1:
            I[i]=i
            continue
        for n in com[i]:
            a.append(n)
            for k in com[i]:
                if k not in a:
                    sim=sim+judge_road_to_sim(G,n,k)
            index[sim/len(com[i])]=n
        I[index[max(index.keys())]]=i
    for i in I:
        com_new[i]=com[I[i]]
    return com_new

def find_com(G, com, node):
    for i in list(com):
        #         print(i)
        for n in list(com[i]):
            #             print(n)
            if node == n:
                return i
    return 0

def del_node(node, com):
    for i in list(com):
        for n in list(com[i]):
            if node == n:
                com[i].remove(n)
    return com

def count_uc(G,com,node,c):
    nei=list(G.__getitem__(node))
    center=c
    sim=0
    sim_=0
    for i in com[center]:
        if i in nei:
            sim=sim+judge_road_to_sim(G,node,i)
    for n in nei:
        sim_=sim_+judge_road_to_sim(G,node,n)
    return (sim/sim_)

def find_vp(G,com,node):
    nei=list(G.__getitem__(node))
    a=set()
    for i in nei:
        b=find_com(G,com,i)
        if b !=0:
            a.add(b)
    return a

def number_of_com(G,com,node,node_,m):
    time=0
    times=0
    for i in com:
        for k in com[i]:
            if k ==node:
                time=time+1
            if k==node_:
                times=times+1
    try:all=(1/(time*times))*(G[node][node_]['value']-(len(G[node])*len(G[node_]))/m)
    except:all=0
    return all
def count_eqk(G,com):
    m=2*nx.number_of_edges(G)
    eqk=0
    for i in com:
        a=[]
        for vp in com[i]:
            a.append(vp)
            for vq in com[i]:
                if vq not in a:
                    eqk=eqk+number_of_com(G,com,vp,vq,m)
    return eqk/m
