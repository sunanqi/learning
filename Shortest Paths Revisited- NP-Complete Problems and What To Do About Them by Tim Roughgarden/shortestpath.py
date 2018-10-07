import datetime
import numpy as np
print('start loading data:', datetime.datetime.now())
file = "g3.txt"
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\4. Shortest Paths Revisited, NP-Complete Problems and What To Do About Them\\' + file) as f:
    lines=f.read().split('\n')
i = 0
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        tmp = [int(t) for t in tmp]
        if i==0:
            n_v = tmp[0]
            n_e = tmp[1]
            i += 1
            print('v and e = ', n_v, n_e)
            A={}
            max_edge = -np.inf
        else:
            A[(tmp[0], tmp[1], 0)] = tmp[2]
            max_edge = max(max_edge, tmp[2])
            i+=1
for i in range(1, n_v+1):
    A[(i,i,0)] = 0
print('finished loading data:', datetime.datetime.now())
print(len(A), max_edge)
B = {}

for k in range(1, n_v+1):
    A0 = A.copy()
    A = {}
    print(k, datetime.datetime.now(), max([A0[ii] for ii in A0]), min([A0[ii] for ii in A0]))
    for i in range(1, n_v+1):
        for j in range(1, n_v+1):
            # A[i, j ,k] = min( A[i,j,k-1] , A[i,k,k-1]+A[k,j,k-1])
            if (i,j,k-1) in A0:
                if (i,k,k-1) in A0 and (k,j,k-1) in A0:
                    if A0[(i,j,k-1)] > A0[(i,k,k-1)]+A0[(k,j,k-1)]:
                        A[(i,j,k)] = A0[(i,k,k-1)]+A0[(k,j,k-1)]
                        B[(i,j)] = k
                    else:
                        A[(i,j,k)] = A0[(i,j,k-1)]
                else:
                    A[(i,j,k)] = A0[(i,j,k-1)]
            elif (i,k,k-1) in A0 and (k,j,k-1) in A0:
                A[(i,j,k)] = A0[(i,k,k-1)]+A0[(k,j,k-1)]
                B[(i,j)] = k
    for diag in range(1, n_v+1):
        if A[(diag, diag, k)] < 0:
            print('has neg cycle', diag)

print('finished forming A:', datetime.datetime.now())

has_no_neg_cycle = False
for i in range(1, n_v+1):
    if A[(i, i, n_v)] < 0:
        has_no_neg_cycle = True
        break
print('has_no_neg_cycle: ', has_no_neg_cycle)
print('finished checking neg cycle:', datetime.datetime.now())

if not has_no_negative_cycles:
    shortest_path = np.inf
    for i in A:
        shortest_path = min(shortest_path, A[i])
    print('shortest_path is: ', shortest_path)
print('finished retrieving shortest path:', datetime.datetime.now())













# a
