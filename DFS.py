from collections import defaultdict
class graph:
    def __init__ (self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v)
        for neg in self.graph[v]:
            if neg not in visited:
                self.DFSUtil(neg,visited)
    def DFS(self,v):
        visited=set()
        self.DFSUtil(v,visited)
g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print ("Following is Depth First Traversal"
" (starting from vertex 2)")
g.DFS(2)       
        
        