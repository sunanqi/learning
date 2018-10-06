def quickSort(A,l,r):
    #print('A,l,r=',A,l,r)
    global n_comparisons
    if r-l==1:
        if A[l]>A[r]:
            A[l], A[r] = A[r], A[l]
        n_comparisons += 1
        #print('n_comparisons',n_comparisons)
        return


    # use median of three as pivot: A[l], A[r], A[l+(r-l)//2]
    if min(A[l], A[r], A[l+(r-l)//2]) < A[r] < max(A[l], A[r], A[l+(r-l)//2]):
        A[l], A[r] = A[r], A[l]
    if min(A[l], A[r], A[l+(r-l)//2]) < A[l+(r-l)//2] < max(A[l], A[r], A[l+(r-l)//2]):
        A[l], A[l+(r-l)//2] = A[l+(r-l)//2], A[l]
    

    # use last element as pivot
    #A[l], A[r] = A[r], A[l]

    p=A[l] #pivot
    n_comparisons += r-l
    #print('n_comparisons',n_comparisons)
    i=l+1
    for j in range(i,r+1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]  #swap A[i] and A[j]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]

    if i-2-l>=1:
        quickSort(A,l,i-2)
    if r-i>=1:
        quickSort(A,i,r)
    return


location = r'F:\Google Drive\coursera\Divide and Conquer, Sorting and Searching, and Randomized Algorithms\QuickSort.txt'
with open(location) as f:
    p=f.read().split('\n')
A=[int(i) for i in p if len(i)]
#A = [10,8,7,6,1,2,3,5,4,9]
n_comparisons = 0
quickSort(A,0,len(A)-1)
print('final=',n_comparisons)
