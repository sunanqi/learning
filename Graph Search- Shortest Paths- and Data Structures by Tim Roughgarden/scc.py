import datetime

def SCC_1(G):
    #print(G)
    explored = [False] * len(G)
    f=[0] * len(G)
    fback = [0] * len(G)
    stack = [iter(range(len(G),0,-1))]
    finish_time = 1
    while stack:
        try:
            child = next(stack[-1])
            #print('try:', child)
            if not explored[child - 1]:
                explored[child - 1] = True
                #reachable_order.append(child)
                # Do whatever you want to do in the visit
                if len(G[child])==0 or min([explored[i-1] for i in G[child]])==1:
                    #print("finish:", child, finish_time)
                    f[child-1] = finish_time
                    finish_time += 1
                else:
                    stack.append(iter([*G[child],child]))
        except StopIteration:
            #print("finish:", child, finish_time)
            if finish_time <= len(G):
                f[child-1] = finish_time
                fback[finish_time-1] = child
                finish_time += 1
            stack.pop()
    return f, fback

def reverseGraph(G):
    n_vertices = len(G)
    #print('len(G)', n_vertices)
    G_rev = {}
    for v in G:
        for head in G[v]:
            if head in G_rev:
                G_rev[head].append(v)
            else:
                G_rev[head] = [v]
    for i in range(1, n_vertices+1):
        if i not in G_rev:
            G_rev[i] = []
    #print('len(G_rev)', len(G_rev))
    return G_rev

def SCC_2(G):
    explored = [False] * len(G)
    SCC={} # the indices are leaders, values are list of SCC from leader
    for i in range(len(G),0,-1):
        if not explored[i-1]:
            explored[i-1] = True
            SCC[i]=[i]  # i is leader
            stack = [iter(G[i])]
            while stack:
                try:
                    child = next(stack[-1])
                    if not explored[child - 1]:
                        explored[child - 1] = True
                        SCC[i].append(child)
                        stack.append(iter(G[child]))
                except StopIteration:
                    stack.pop()
    return SCC

G = {}
n = 875714
file = "SCCsample1.txt"
print(datetime.datetime.now())
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\2. Graph Search, Shortest Paths, and Data Structures\\' + file) as f:
    lines=f.read().split('\n')
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        tmp = [int(i) for i in tmp]
        if tmp[0] not in G:
            G[tmp[0]] = [tmp[1]]
        else:
            G[tmp[0]].append(tmp[1])
for i in range(1, n+1):
    if i not in G:
        G[i] = []

print('G loaded:')
print(datetime.datetime.now())
G_rev = reverseGraph(G)
print('G_rev loaded:')

print(datetime.datetime.now())
f, fback = SCC_1(G_rev)
print('len, min, max:', len(f), min(f), max(f))
print(datetime.datetime.now())

G_updated={}
for i in G_rev:
    G_updated[f[i-1]] = [f[l-1] for l in G_rev[i]]
G_updated = reverseGraph(G_updated)
print('G_updated:')

SCC = SCC_2(G_updated)
#print('SCC:',SCC)
SCC_summary = {i:len(SCC[i]) for i in SCC}
SCC_summary2 = {i:len(set(SCC[i])) for i in SCC}

SCC_sorted = sorted(SCC_summary.items(), key=lambda kv: kv[1], reverse=True)
SCC_sorted2 = sorted(SCC_summary2.items(), key=lambda kv: kv[1], reverse=True)

print(SCC_sorted[:5])
print(SCC_sorted2[:5])

# SCC_original: get the vertex index of origial Graph
SCC_original = {}
for v in SCC:
    SCC_original[fback[v-1]] = [fback[i-1] for i in SCC[v]]

#f[child-1] = finish_time
#fback[finish_time-1] = child

'''
2018-09-20 00:09:59.540142
G loaded:
2018-09-20 00:10:10.749310
G_rev loaded:
2018-09-20 00:10:13.758383
len, min, max: 875714 1 875714
2018-09-20 00:10:17.555888
G_updated:
[(615986, 434821), (617403, 968), (798411, 459), (43840, 313), (709991, 211)]
'''
