import sys
sys.setrecursionlimit(1500)
import numpy as np
import datetime
print('start loading data:', datetime.datetime.now())
file = "huffman.txt"
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\3. Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\\' + file) as f:
    lines=f.read().split('\n')
i = -1
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        tmp = [int(t) for t in tmp]
        if i==-1:
            n_symbol = tmp[0]
            i += 1
            W = [0]*n_symbol
        else:
            W[i] = tmp[0]
            i+=1

#encoding = np.vstack(range(n_symbol), range(n_symbol)).T

def huffman(W):
    '''
    input: list of weights
    output: list of string in bit code
    '''
    if len(W) == 2:
        if W[0]>=W[1]:
            return ['0','1']
        else:
            return ['1','0']
    ind = [i[0] for i in sorted(enumerate(W), key=lambda x:x[1], reverse=True)]
    #ind = np.argsort(W)
    W_sorted = [W[i] for i in ind]
    Wcombo = W_sorted[:-1]
    Wcombo[-1] = W_sorted[-1]+W_sorted[-2]
    Rtmp = huffman(Wcombo)
    Rtmp.append(Rtmp[-1]+'1')
    Rtmp[-2] += '0'
    R = ['']*len(W)
    for i,j in enumerate(ind):
        R[j] = Rtmp[i]
    return R

#print(huffman(W))
print(set([len(i) for i in huffman(W)]))
