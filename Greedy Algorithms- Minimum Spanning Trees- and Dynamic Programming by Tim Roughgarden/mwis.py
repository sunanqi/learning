import datetime
print('start loading data:', datetime.datetime.now())
file = "mwis.txt"
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
            W = [0]*n_v
        else:
            W[i] = tmp[0]
            i+=1
#print(W)
sw = [0]*n_v #sum_weight
sw[0], sw[1] = W[0], max(W[0],W[1])
for i in range(2, n_v):
    sw[i] = max(sw[i-1], sw[i-2]+W[i])

#print(sw)

is_selected = [False]*n_v
i = n_v-1
while True:
    if i==0:
        is_selected[i] = True
        break
    elif i==1:
        is_selected[0], is_selected[1] = (True, False) if W[0]>W[1] else (False, True)
        break
    if sw[i-1] > sw[i-2]+W[i]:
        is_selected[i] = False
        i -= 1
    else:
        is_selected[i] = True
        is_selected[i-1] = False
        i -= 2

#print(is_selected)
print([is_selected[i-1] for i in [1, 2, 3, 4, 17, 117, 517, 997]])





# a
