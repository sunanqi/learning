#import matplotlib.pyplot
import datetime
#import numpy as np
d = lambda a,b : ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
d2 = lambda a,b : (a[0]-b[0])**2+(a[1]-b[1])**2
print('start loading data:', datetime.datetime.now())
file = "nn.txt"
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
            G={}
        else:
            G[int(tmp[0])] = (tmp[1], tmp[2])
            i+=1
#print(G)
print('finished loading data:', datetime.datetime.now())

P = {}
origin_idx, origin_pos = 1, G[1]
curr_idx, curr_pos = 1, G[1]
del G[curr_idx]
cnt = 0
while G:  # remove curr_index?
    cnt += 1
    if cnt % 10000 == 0:
        print(cnt, ' of ', n_city, datetime.datetime.now())
    flag = False
    for idx in G:
        if flag == False:
            min_dist = d2(curr_pos, G[idx])
            next_idx = idx
            flag = True
        else:
            if d2(curr_pos, G[idx]) < min_dist:
                min_dist = d2(curr_pos, G[idx])
                next_idx = idx
            elif d2(curr_pos, G[idx]) == min_dist:
                next_idx = min(next_idx, idx)
    P[(curr_idx, next_idx)] = min_dist
    curr_idx, curr_pos = next_idx, G[next_idx]
    del G[curr_idx]

P[(curr_idx, origin_idx)] = d(curr_pos, origin_pos)
tsp = sum([P[i]**0.5 for i in P])
print('tsp= ', tsp, datetime.datetime.now())

# tsp = 1203406.5012

'''
if using sqrt(d^2) as distance comparison:
start loading data: 2018-10-04 10:59:58.385236
finished loading data: 2018-10-04 10:59:58.604816
10000  of  33708 2018-10-04 11:07:41.656917
20000  of  33708 2018-10-04 11:13:13.948345
30000  of  33708 2018-10-04 11:15:46.962159
tsp=  1203406.5012708856 2018-10-04 11:15:58.893876

if using (d^2) as distance comparison:
start loading data: 2018-10-04 12:24:32.420516
finished loading data: 2018-10-04 12:24:32.658146
10000  of  33708 2018-10-04 12:31:18.144194
20000  of  33708 2018-10-04 12:35:54.324440
30000  of  33708 2018-10-04 12:38:09.553000
tsp=  1190635.8999266396 2018-10-04 12:38:18.483745
'''
