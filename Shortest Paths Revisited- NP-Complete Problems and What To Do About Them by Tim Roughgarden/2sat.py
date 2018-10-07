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

print('start loading data:', datetime.datetime.now())
file = "2sat6.txt"
print('file name: ', file)
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\4. Shortest Paths Revisited, NP-Complete Problems and What To Do About Them\\' + file) as f:
    lines=f.read().split('\n')
i = 0
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        tmp = [int(t) for t in tmp]
        if i==0:
            nv = int(tmp[0])  # number of variables
            print('there are ', nv, 'variables')
            i += 1
            G = {v:[] for v in range(1,nv*2+1)}  # total nv*2 vertices
        else:
            x, y = tmp[0], tmp[1]
            if x<0 and y<0:  # not x or not y: x ==> not y; y ==> not x
                G[-x] += [-y+nv]
                G[-y] += [-x+nv]
            elif x<0 and y>0:  # not x or y: x ==> y; not y ==> not x
                G[-x] += [y]
                G[y+nv] += [-x+nv]
            elif x>0 and y<0:   # x or not y: not x ==> not y; y ==> x
                G[x+nv] += [-y+nv]
                G[-y] += [x]
            elif x>0 and y>0:   # x or y: not x ==> y; not y ==> x
                G[x+nv] += [y]
                G[y+nv] += [x]
            else:
                print('data error?')
                break
#print(G)

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
SCC_original = {}
for v in SCC:
    SCC_original[fback[v-1]] = [fback[i-1] for i in SCC[v]]

satisfiable = True
for i in SCC_original:
    for j in SCC_original[i]:
        if j+nv in SCC_original[i] or j-nv in SCC_original[i]:
            print('i, j, SCC[i]=', i, j, SCC_original[i])
            satisfiable = False
            break
print('satisfiable=', satisfiable)

#print(SCC)
