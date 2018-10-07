import numpy as np
import datetime
print('start loading data:', datetime.datetime.now())
file = "clustering1.txt"
print('start loading data:', datetime.datetime.now())
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\3. Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\\' + file) as f:
    lines=f.read().split('\n')
i = -1
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        tmp = [int(t) for t in tmp]
        if i==-1:
            n_v = tmp[0]
            i += 1
            G = np.zeros(shape = (n_v*(n_v-1)//2,3))
        else:
            G[i,:] = tmp
            i+=1

print(G, G.shape)
print('finish loading data, start calculating:', datetime.datetime.now())

k=4
n_cluster = n_v # initially each vertice is a cluster
cluster = np.column_stack((range(1,n_v+1), range(1,n_v+1)))
# ndarray: first column is vertice number, second column is cluster number

G = G[np.argsort(G[:,2])] # sort edges by distances

for i in range(len(G)):
    v1, c1 = tuple(cluster[cluster[:,0]==G[i,0],:][0])
    v2, c2 = tuple(cluster[cluster[:,0]==G[i,1],:][0])
    if c1 != c2: # if two vertices belong to different cluster
        if n_cluster==k:
            max_spacing = G[i,2]
            break
        cluster[cluster[:,1]==c1, 1] = c2
        n_cluster -= 1

#print(G)
print('max_spacing=', max_spacing)
for gr in set(cluster[:,1]):
    print('group ', gr, 'has ', cluster[cluster[:,1]==gr].shape[0], 'vertices')
