import matplotlib.pyplot
import datetime
import numpy as np
d = lambda a,b : ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
print('start loading data:', datetime.datetime.now())
file = "tsp.txt"
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\4. Shortest Paths Revisited, NP-Complete Problems and What To Do About Them\\' + file) as f:
    lines=f.read().split('\n')
i = 0
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        tmp = [float(t) for t in tmp]
        if i==0:
            n_city = int(tmp[0])
            i += 1
            G=[]
        else:
            G.append((tmp[0], tmp[1]))
            i+=1
#print(G)

# Base case
Anew={}
for j in range(2,n_city+1):
    Anew[(tuple([1,j]), j)]=d(G[1-1], G[j-1])

# recurrence
for m in range(3, n_city+1):
    print('m=', m, datetime.datetime.now())
    A = Anew.copy()
    Anew={}
    for s in itertools.combinations(range(2,n_city+1), m-1):  # s has m-1 elements
        s1 = tuple(sorted(list(s) + [1]))   # s1 has m elements
        for j in s:
            if j != 1:
                sj = tuple(sorted([i for i in s1 if i!=j]))  # sj has m-1 elements
                Asj_flag = False
                for k in s:
                    if (sj, k) in A:
                        if Asj_flag == False:
                            Asj = A[(sj, k)] + d(G[k-1], G[j-1])
                            Asj_flag = True
                        else:
                            Asj = min(Asj, A[(sj, k)] + d(G[k-1], G[j-1]))
                if Asj_flag == True:
                    Anew[(s1, j)] = Asj

tsp_flag = False
for k in range(2, n_city+1):
    if tsp_flag==False:
        tsp = Anew[tuple(range(1,n_city+1)), k] + d(G[k-1], G[0])
        tsp_flag = True
    else:
        tsp = min(tsp, Anew[tuple(range(1,n_city+1)), k] + d(G[k-1], G[0]))

# tsp = 26442.73030895475

matplotlib.pyplot.scatter([i[0] for i in G], [i[1] for i in G])
