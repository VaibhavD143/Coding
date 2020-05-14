class Graph(): 
  
    def __init__(self, v): 
        self.v = v 
        self.graph = [[0 for column in range(v)]  
                    for row in range(v)] 
  
    def Solution(self, dist): 
        print("Vertex \tDistance from Source")
        for v in range(self.v): 
            print(v,"\t", dist[v])

    def minDistance(self, dist, vis): 
  
        min = 100000000 
  
        for v in range(self.v): 
            if dist[v] < min and vis[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    def dijkstra(self, src): 
  
        dist = [100000000] * self.v 
        dist[src] = 0
        vis = [False] * self.v
  
        for cout in range(self.v): 

            u = self.minDistance(dist, vis) 
  
            vis[u] = True
  
            for v in range(self.v): 
                if self.graph[u][v] > 0 and vis[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 
  
        self.printSolution(dist) 
  
# Driver program
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
  
g.dijkstra(0);