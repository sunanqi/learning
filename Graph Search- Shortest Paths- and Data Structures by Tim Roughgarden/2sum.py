import datetime

print(datetime.datetime.now())

file = "algo1-programming_prob-2sum.txt"
#print(datetime.datetime.now())
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\2. Graph Search, Shortest Paths, and Data Structures\\' + file) as f:
    lines=f.read().split('\n')

#t=28662257282
T = []
d={}
count=1
for l in lines:
    if count%10000==0:
        print(count, datetime.datetime.now())
    if l:
        tmp = int(l.strip())
        T.extend([t for t in range(-10000, 10001) if t-tmp in d])
        #print(T)
        d[tmp]=True
    count+=1

print(len(set(T)))
#print(found)
print(datetime.datetime.now())
