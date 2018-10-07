import datetime
print('start loading data:', datetime.datetime.now())
file = "knapsack_big.txt"
with open('F:\\Google Drive\\coursera\\Algorithms - Tim Roughgarden\\3. Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\\' + file) as f:
    lines=f.read().split('\n')
i = -1
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        tmp = [int(t) for t in tmp]
        if i==-1:
            knapsack_size = tmp[0]
            number_of_items = tmp[1]
            i += 1
            items = [(0,0)]*number_of_items
        else:
            items[i] = (tmp[0], tmp[1])
            # value, weight
            i+=1
print('finished loading data:', datetime.datetime.now())

stack = [(number_of_items, knapsack_size)]
solution = {}
while stack:
    if stack[-1] in solution:
        stack.pop()
    elif stack[-1][0]==0:
        if not stack[-1] in solution:
            solution[stack[-1]] = 0
            stack.pop()
    else: # calculate V(i,x)
        a = stack[-1]  # to be calculated
        if a[1] < items[a[0]-1][1]:
            # only choice is V(i-1, x)
            if (a[0]-1, a[1]) in solution:
                solution[stack[-1]] = solution[(a[0]-1, a[1])]
                stack.pop()
            else:
                stack.append((a[0]-1, a[1]))
        else:
            if ((a[0]-1, a[1]) in solution) and ((a[0]-1, a[1]-items[a[0]-1][1]) in solution):
                solution[stack[-1]] = max(solution[(a[0]-1, a[1])], solution[(a[0]-1, a[1]-items[a[0]-1][1])]+items[a[0]-1][0])
            else:
                if (a[0]-1, a[1]) not in solution:
                    stack.append((a[0]-1, a[1]))
                if (a[0]-1, a[1]-items[a[0]-1][1]) not in solution:
                    stack.append((a[0]-1, a[1]-items[a[0]-1][1]))

print('finished calculating:', datetime.datetime.now())
print(len(solution))
print(solution[(number_of_items, knapsack_size)])

#kanpsack1: solution[(100,10000)] Out[276]: 2493893
#kanpsack_big: solution[(2000,200000)] Out[276]: 4243395
