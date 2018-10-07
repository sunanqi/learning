import numpy as np
import datetime

def distance(v1, v2):
# v1 = (T, T, T, F, F, F, F, F, T, T, F, T, F, F, T, T, T, T, F, F, T, T, T, T)
# v2 = (F, T, T, F, F, T, T, F, F, T, F, T, T, T, T, T, T, F, T, F, T, T, F, T)
    return(sum([i[0]!=i[1] for i in zip(v1, v2)]))

def has_dup(G):
    tmpG = {}
    for v in G:
        if v not in tmpG:
            tmpG[v]=1
        else:
            return True
    return False

def DFS(G,s):
    explored = [False] * len(G)
    explored[s-1] = True
    f=[0] * len(G)
    #reachable_order=[s-1]
    stack = [iter(G[s])]
    while stack:
        try:
            child = next(stack[-1])
            if not explored[child - 1]:
                explored[child - 1] = True
                #reachable_order.append(child)
                # Do whatever you want to do in the visit
                stack.append(iter(G[child]))
        except StopIteration:
            stack.pop()
    return explored#, reachable_order

print('start loading data:', datetime.datetime.now())
file = "clustering_big.txt"
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\3. Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\\' + file) as f:
    lines=f.read().split('\n')
i = 0
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        if i==0:
            #n_v = int(tmp[0])  there are dup in 200k nodes
            n_bits = int(tmp[1])
            i += 1
            G = {}
        else:
            tmp = tuple([True if int(t)==1 else False for t in tmp])
            if tmp not in G:
                G[tmp] = i  # key = vertex value in bits, value: vertex number
                i+=1
n_v = i-1
print('finished loading data:', datetime.datetime.now())

G1 = {}
# G1 is an adjacency list of a graph
for key in G:
    for i in range(len(key)):
        for j in range(i, len(key)):
            tmp = list(key)
            if i==j:
                tmp[i] = not tmp[i]
            else:
                tmp[i] = not tmp[i]
                tmp[j] = not tmp[j]
            if tuple(tmp) in G:
                if G[key] not in G1:
                    G1[G[key]] = [G[tuple(tmp)]]
                else:
                    G1[G[key]].append(G[tuple(tmp)])

for i in range(1, n_v+1):
    if i not in G1:
        G1[i] = []
print('finished calculating G1:', datetime.datetime.now())

cluster = np.zeros(shape=n_v)
# index+1 = vertex number; value = cluster number. initial value=0
cluster_number=0
while 0 in cluster:
    cluster_number += 1
    s = np.where(cluster==0)[0][0]
    explored = DFS(G1, s+1)
    if len(set(cluster[explored]))>1:
        print('error')
        break
    cluster[explored]=cluster_number
print('finished clustering:', datetime.datetime.now())
#print(cluster)
#print(set(cluster))
print(len(set(cluster)))
print(cluster_number)

# 6118
