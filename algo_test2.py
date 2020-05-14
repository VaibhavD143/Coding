import random
class Graph(): 
  
    def __init__(self, v): 
        self.v = v 
        self.graph = [[0 for column in range(v)]  
                    for row in range(v)] 
    def next_node(self, dist, vis): 
  
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

            u = self.next_node(dist, vis) 
  
            vis[u] = True
  
            for v in range(self.v): 
                if self.graph[u][v] > 0 and vis[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                    dist[v] = dist[u] + self.graph[u][v] 
  
        return dist
  
# Driver program
# g = Graph(9) 
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
#         [4, 0, 8, 0, 0, 0, 0, 11, 0], 
#         [0, 8, 0, 7, 0, 4, 0, 0, 2], 
#         [0, 0, 7, 0, 9, 14, 0, 0, 0], 
#         [0, 0, 0, 9, 0, 10, 0, 0, 0], 
#         [0, 0, 4, 14, 10, 0, 2, 0, 0], 
#         [0, 0, 0, 0, 0, 2, 0, 1, 6], 
#         [8, 11, 0, 0, 0, 0, 1, 0, 7], 
#         [0, 0, 2, 0, 0, 0, 6, 7, 0] 
#         ];
def driver(k,x,g):
    n=10000
    # k=1
    # x = 6
    # g = Graph(n)
    # g.graph = [ [0,1,2,0,0,0],
    #             [1,0,0,6,0,0],
    #             [2,0,0,40,2,0],
    #             [0,6,40,0,10,4],
    #             [0,0,2,10,0,5],
    #             [0,0,0,4,5,0]]
    s_dist = g.dijkstra(0)
    e_dist = g.dijkstra(n-1)

    print(s_dist,e_dist)
    
    min_dis= 100000000000000
    
    for i in range(n):
        if i >= (n//2) and i <= (n//2)+k-1 and e_dist[i] <= x:
            if min_dis > s_dist[i]+e_dist[i]:
                min_dis = s_dist[i]+e_dist[i]
        
    return min_dis if min_dis != 100000000000000 else -1


def input():
    n=10000
    b = []
    w = []
    a = []
    m=0
    for i in range(2,n):
        j = random.randint(1,1000)%i
        while j >=0:
            b.append(j)
            a.append(i)
            w.append((random.randint(1,1000)%433)+2)
            m+=1
            if j>0:
                j = random.randint(1,1000)%j
            else:
                j = -1
    print(a,b,w)
    k=10
    x = 3000
    g = Graph(n)
    # g.graph = [[0]*n for _ in range(n)]
    for i in range(len(a)):
        g.graph[a[i]][b[i]] = w[i]
        g.graph[b[i]][a[i]] = w[i]

    print(driver(k,x,g))
print(input())