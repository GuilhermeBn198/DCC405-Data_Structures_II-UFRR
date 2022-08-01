

class Graph:

    def __init__(self,vertices):
        self.V=vertices #numero de vertices
        self.graph=[]#vetor vazio definido para armazenar as arestas entre vertices

    def addEdge(self, u, v):
        self.graph.append([u,v])

    def DFSUtil(self, v, visited):
       visited[v]=True
       print(v, end = ' ')

       for i in self.graph:
          if v==i[0]:
             if visited[i[1]] == False:
                self.DFSUtil(i[1], visited)

    def DFS(self, v):
       visited = [False] * (self.V)

       #ordena conforme primeiro vertice das arestas
       self.graph.sort()

       self.DFSUtil(v, visited)

g=Graph(6)

#A=0
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(0,4)

#B=1
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)

#C=2
g.addEdge(2,3)
g.addEdge(2,4)

#D=3
g.addEdge(3,4)
g.addEdge(3,5)
#E=4

g.DFS(0)