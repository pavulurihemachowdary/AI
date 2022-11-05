from sys import maxsize
from itertools import permutations
V=4
def TVS(graph,s):
    vertex=[]
    for i in range(V):
       if(i!=s):
           vertex.append(i)
    minpath=maxsize
    nextper=permutations(vertex)
    for i in nextper:
        
        currentpath=0
        k=s
        for j in i:
            currentpath+=graph[k][j]
            k=j
        currentpath+=graph[k][s]
        minpath=min(minpath,currentpath)
    return minpath
if __name__ == "__main__":
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
    s=0
    print(TVS(graph,s))