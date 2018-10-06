import random
import copy

def contraction():
    '''
    input: graph
    output: contracted graph
    '''
    global d
    tmp = random.choices(list(d.items()), weights=[len(t) for t in d.values()], k=1)[0]
    v1,v2 = tmp[0], random.choice(tmp[1])
    new_vertex = max(d)+1
    new_vertex_connected = d[v1]+d[v2]
    # remove self loop for new (combined) vertex
    new_vertex_connected = [v for v in new_vertex_connected if v!=v1 if v!=v2]
    del d[v1]
    del d[v2]
    
    # update old vertices
    for v,e in d.items():
        d[v] = [new_vertex if t in (v1,v2) else t for t in e]
    
    # add new (combined) vertex to the graph
    d[new_vertex] = new_vertex_connected
    #print(d)
    


with open(r'F:\Google Drive\coursera\Divide and Conquer, Sorting and Searching, and Randomized Algorithms\kargerMinCut.txt') as f:
    g=f.read().split('\n')
for i in range(len(g)):
    g[i] = g[i].split()
    g[i] = [int(j) for j in g[i]]
g=[i for i in g if len(i)>0]
d0={}
for i in range(len(g)):
    d0[g[i][0]] = g[i][1:]

sim = 100
result = []
for s in range(sim):
    d = copy.deepcopy(d0)
    for i in range(len(g)-2):
        contraction()
    result.append(len(d[list(d.keys())[0]]))

#print(result)
results = {x:result.count(x) for x in result}
print(results)
