class Graph:

    AL  = []

    visitStack = []
    edges = []
    backEdges = []

    def __init__(self, Graph):
        self.AL  = Graph

    def  DFS(self):
        self.edges.append(0)
        self.visitStack.append(0)
        self.dfs(0)
        print("edges")
        print("↓↓↓↓↓")
        for i in self.edges:
            print(i)
        
        print("\nback edges")
        print("↓↓↓↓↓↓")

        for i in self.backEdges:
            print(i)

    def dfs(self, point):

        for i in range(len(self.AL[point])):

            if(self.AL[point][i] in self.visitStack):
                self.backEdges.append( str(point) + "→" + str(i) )

            if(not(self.AL[point][i] in self.edges)):
                
                self.visitStack.append(self.AL[point][i])
                self.edges.append(self.AL[point][i])
                
                self.dfs(self.AL[point][i])
                
        self.visitStack.pop()
            


#takes in Adjacency list
#TODO fix back edges
g = Graph([[1,2], [2,3,4], [0,1,3], [1,2,4],[1,3]])

g.DFS()