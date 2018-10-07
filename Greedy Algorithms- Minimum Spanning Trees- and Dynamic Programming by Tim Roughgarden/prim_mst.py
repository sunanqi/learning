import numpy as np
import datetime
file = "edges.txt"
print('start loading data:', datetime.datetime.now())
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\3. Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\\' + file) as f:
    lines=f.read().split('\n')
i = -1
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        tmp = [int(t) for t in tmp]
        if i==-1:
            v, e = tmp[0], tmp[1]
            G = np.zeros(shape = (e,3))
            i += 1
        else:
            G[i,:] = tmp
            i += 1

#print(G, G.shape)
print('finish loading data, start calculating:', datetime.datetime.now())

V = list(range(1,501))
X = [1]
T = []
while len(X) != len(V):
    G1 = G[np.in1d(G[:, 0], X)]
    G1 = G1[np.in1d(G1[:, 1], [x for x in V if x not in X])]
    G2 = G[np.in1d(G[:, 1], X)]
    G2 = G2[np.in1d(G2[:, 0], [x for x in V if x not in X])]
    G1 = np.vstack((G1,G2))
    G1min = G1[np.argmin(G1[:,2]),:]
    #print(G1min)
    if G1min[0] in X:
        X.append(G1min[1])
    else:
        X.append(G1min[0])
    T.append(G1min[2])
    #print(len(X))

print('done:', datetime.datetime.now())
print(len(X))
print(len(T))
print(sum(T))

# sum(T) = -3612829
