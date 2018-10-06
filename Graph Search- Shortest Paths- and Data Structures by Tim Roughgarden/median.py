import datetime
import math
import random

def printheap(h): # need re-write
    c, curr_line, last_line_length = 1, 1, len(h)//2+1
    print(' '*(last_line_length-curr_line+1), end='')
    for i in range(len(h)):
        if c > curr_line:
            print('')
            curr_line *= 2
            print(' '*(last_line_length-curr_line), end='')
            c=1
        print(h[i],end=' ')
        c += 1
    print('\n')

def heapMinInsert(h, v):
    h.append(v)
    curr = len(h)-1
    while True:
        #print(h)
        if h[curr] < h[(curr-1)//2]:
            h[curr], h[(curr-1)//2] = h[(curr-1)//2], h[curr]
            curr = (curr-1)//2
            if curr==0:
                break
        else:
            break
    return h

def heapMaxInsert(h, v):
    h.append(v)
    curr = len(h)-1
    while True:
        #print(h)
        if h[curr] > h[(curr-1)//2]:
            h[curr], h[(curr-1)//2] = h[(curr-1)//2], h[curr]
            curr = (curr-1)//2
            if curr==0:
                break
        else:
            break
    return h

def heapMinExtractMin(h):
    h[0] = h.pop()
    l = len(h)
    curr = 0
    while curr*2+1 <= l-1:
        #printheap(h)
        if (curr*2+2 <= l-1) and h[curr] > min(h[curr*2+1], h[curr*2+2]):
            if h[curr*2+1] < h[curr*2+2]:
                h[curr], h[curr*2+1] = h[curr*2+1], h[curr]
                curr = curr*2+1
                continue
            else:
                h[curr], h[curr*2+2] = h[curr*2+2], h[curr]
                curr = curr*2+2
                continue
        if curr*2+1 == l-1 and h[curr] > h[curr*2+1]:
            h[curr], h[curr*2+1] = h[curr*2+1], h[curr]
            break
        break
    return h

def heapMaxExtractMax(h):
    h[0] = h.pop()
    l = len(h)
    curr = 0
    while curr*2+1 <= l-1:
        #printheap(h)
        if (curr*2+2 <= l-1) and h[curr] < max(h[curr*2+1], h[curr*2+2]):
            if h[curr*2+1] > h[curr*2+2]:
                h[curr], h[curr*2+1] = h[curr*2+1], h[curr]
                curr = curr*2+1
                continue
            else:
                h[curr], h[curr*2+2] = h[curr*2+2], h[curr]
                curr = curr*2+2
                continue
        if curr*2+1 == l-1 and h[curr] < h[curr*2+1]:
            h[curr], h[curr*2+1] = h[curr*2+1], h[curr]
            break
        break
    return h

def doubleHeapInsert(heapH, heapL, v):
    pass

file = "Median.txt"
#print(datetime.datetime.now())
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\2. Graph Search, Shortest Paths, and Data Structures\\' + file) as f:
    lines=f.read().split('\n')
row = 1
for l in lines:
    if l:
        if row==1:
            n1 = int(l.strip())
            row +=1
            medlist = [n1]
        elif row==2:
            n2 = int(l.strip())
            heapmax = [min(n1,n2)]
            heapmin = [max(n1,n2)]
            medlist.append(min(n1,n2))
            row +=1
        else:
            n = int(l.strip())
            if n > heapmin[0]:
                heapMinInsert(heapmin, n)
            elif n < heapmax[0]:
                heapMaxInsert(heapmax, n)
            else:
                if len(heapmin)<len(heapmax):
                    heapMinInsert(heapmin, n)
                else:
                    heapMaxInsert(heapmax, n)
            #print('heapmax=', heapmax)
            #print('heapmin=', heapmin)
            #print('\n')
            if len(heapmin)-len(heapmax)==1:
                heapMaxInsert(heapmax, heapmin[0])
                heapMinExtractMin(heapmin)
            if len(heapmax)-len(heapmin)==2:
                heapMinInsert(heapmin, heapmax[0])
                heapMaxExtractMax(heapmax)
            #print('heapmax=', heapmax)
            #print('heapmin=', heapmin)
            #print('\n')
            medlist.append(heapmax[0])

print(sum(medlist))
# result is 46831213


#heapmin = [1,2,3,4,5,6,7,8,9]
#heapmin = heapMinInsert(heapmin, 0)
#print(heapmin)

#heapmax = [8,7,6,5,4,3,2,1]
#heapmax = heapMaxInsert(heapmax, 20)
#print(heapmax)

#heapmax = [i for i in range(11)]
#random.shuffle(heapmax)
#heapmin = heapMaxExtractMax(heapmax)
#printheap(heapmax)
