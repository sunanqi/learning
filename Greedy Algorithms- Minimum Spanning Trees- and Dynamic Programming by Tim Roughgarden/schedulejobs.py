import numpy as np
file = "jobs.txt"
#print(datetime.datetime.now())
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\3. Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\\' + file) as f:
    lines=f.read().split('\n')
i = 0
for l in range(len(lines)):
    if lines[l]:
        if i==0:
            n_jobs = int(lines[l])
            print(n_jobs)
            jobs = np.zeros(shape=(n_jobs,4))
            i += 1
        else:
            tmp = lines[l].split()
            tmp = [int(k) for k in tmp]
            jobs[i-1,0:2] = tmp
            i+=1

jobs[:, 2] = jobs[:, 0] - jobs[:, 1]
ind = np.lexsort((jobs[:,0], jobs[:,2]))
jobs = jobs[ind][::-1]
jobs[:, 3] = np.cumsum(jobs[:, 1])
wct_difference = np.dot(jobs[:, 0], jobs[:,3])

jobs[:, 2] = jobs[:, 0] / jobs[:, 1]
ind = np.lexsort((jobs[:,0], jobs[:,2]))
jobs = jobs[ind][::-1]
jobs[:, 3] = np.cumsum(jobs[:, 1])
wct_ratio = np.dot(jobs[:, 0], jobs[:,3])

#print(jobs)
print('wct_difference=', wct_difference)
print('wct_ratio=', wct_ratio)

#double check ordering
for r in range(jobs.shape[0]-1):
    if jobs[(r,2)] < jobs[(r+1,2)]:
        print('error')
        break
    elif (jobs[(r,2)] == jobs[(r+1,2)]) and (jobs[(r,0)] < jobs[(r+1,0)]):
        print('error')
        break
else:
    print("ok")
