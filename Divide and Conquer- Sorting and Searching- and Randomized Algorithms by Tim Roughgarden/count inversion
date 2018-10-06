def countInversion(l):
    '''
    input: list
    output: num_inversion and sorted list
    '''
    if len(l)==1:
        return 0, l
    if len(l)==2:
        return l[0]>l[1], [min(l), max(l)]
    n = len(l)
    leftInversion, leftSorted = countInversion(l[:n//2])
    rightInversion, rightSorted = countInversion(l[n//2:])

    # calculate split leftInversion
    i = 0; j = 0
    li = len(leftSorted); lr = len(rightSorted)
    inv = leftInversion+rightInversion;
    sortedList = []
    flag = True
    while flag:
        if leftSorted[i] < rightSorted[j]:
            sortedList += [leftSorted[i]]
            if i < li-1:
                i+=1
            else:
                sortedList += rightSorted[j:]
                flag=False
        else: # li[i] > lr[j]
            sortedList += [rightSorted[j]]
            inv += n//2-i
            if j < lr-1:
                j+=1
            else:
                sortedList += leftSorted[i:]
                flag = False
    return inv, sortedList

#l=[6,4,5,3,1,2]
with open(r'F:\Google Drive\coursera\Divide and Conquer, Sorting and Searching, and Randomized Algorithms\IntegerArray.txt') as f:
    p=f.read().split('\n')
q=[int(i) for i in p if len(i)]
print(len(q),min(q),max(q))
print(countInversion(q)[0])
