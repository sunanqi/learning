import math

def DijkstraShortestPath(G, s):
    V = set(range(1,len(G)+1))
    visited = {s}
    unvisited = V-visited
    ShortestPath = {}
    ShortestPath[s] = 0
    while unvisited:
        #print(visited)
        dist = math.inf
        for i in visited:
            for j in unvisited:
                try:
                    if ShortestPath[i]+G[i][j]<dist:
                        dist = ShortestPath[i]+G[i][j]
                        candidate=j
                except:
                    pass
        ShortestPath[candidate] = dist
        visited = visited.union({candidate})
        unvisited -= {candidate}
    return ShortestPath

G = {}
n = 200
with open(r'F:\Google Drive\coursera\Algorithms - Tim Roughgarden\2. Graph Search, Shortest Paths, and Data Structures\dijkstraData.txt') as f:
    lines=f.read().split('\n')
for l in range(len(lines)):
    if lines[l]:
        tmp = lines[l].split()
        #tmp = [int(i) for i in tmp]
        if int(tmp[0]) not in G:
            G[int(tmp[0])] = {int(v.split(',')[0]):int(v.split(',')[1]) for v in tmp[1:]}
        else:
            G[int(tmp[0])].append(tmp[1:])
for i in range(1, n+1):
    if i not in G:
        G[i] = []

ShortestPath = DijkstraShortestPath(G,1)
print([ShortestPath[i] for i in [7,37,59,82,99,115,133,165,188,197]])
