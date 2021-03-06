import random
from collections import defaultdict 


class Heap(): 

	def __init__(self): 
		self.array = [] 
		self.size = 0
		self.pos = [] 

	def newMinHeapNode(self, v, dist): 
		minHeapNode = [v, dist] 
		return minHeapNode 

	def swapMinHeapNode(self,a, b): 
		t = self.array[a] 
		self.array[a] = self.array[b] 
		self.array[b] = t 

	def minHeapify(self, idx): 
		smallest = idx 
		left = 2*idx + 1
		right = 2*idx + 2

		if left < self.size and self.array[left][1] < self.array[smallest][1]: 
			smallest = left 

		if right < self.size and self.array[right][1] < self.array[smallest][1]: 
			smallest = right 

		if smallest != idx: 

			self.pos[ self.array[smallest][0] ] = idx 
			self.pos[ self.array[idx][0] ] = smallest 

			self.swapMinHeapNode(smallest, idx) 

			self.minHeapify(smallest) 

	def extractMin(self): 

		if self.isEmpty() == True: 
			return

		root = self.array[0] 

		lastNode = self.array[self.size - 1] 
		self.array[0] = lastNode 

		self.pos[lastNode[0]] = 0
		self.pos[root[0]] = self.size - 1

		self.size -= 1
		self.minHeapify(0) 

		return root 

	def isEmpty(self): 
		return True if self.size == 0 else False

	def decreaseKey(self, v, dist): 


		i = self.pos[v] 

		self.array[i][1] = dist 

		while i > 0 and self.array[i][1] < self.array[(i - 1)//2][1]: 

			self.pos[ self.array[i][0] ] = (i-1)//2
			self.pos[ self.array[(i-1)//2][0] ] = i 
			self.swapMinHeapNode(i, (i - 1)//2 ) 

			i = (i - 1) //2

	def isInMinHeap(self, v): 

		if self.pos[v] < self.size: 
			return True
		return False




class Graph(): 

	def __init__(self, V): 
		self.V = V 
		self.graph = defaultdict(list) 

	def addEdge(self, src, dest, weight): 

		newNode = [dest, weight] 
		self.graph[src].insert(0, newNode) 
		newNode = [src, weight] 
		self.graph[dest].insert(0, newNode) 

	def dijkstra(self, src): 

		V = self.V # Get the number of vertices in graph 
		dist = [] # dist values used to pick minimum 
					# weight edge in cut 

		minHeap = Heap() 

		for v in range(V): 
			dist.append(int(1e10)) 
			minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
			minHeap.pos.append(v) 

		minHeap.pos[src] = src 
		dist[src] = 0
		minHeap.decreaseKey(src, dist[src]) 
		minHeap.size = V

		while minHeap.isEmpty() == False: 

			newHeapNode = minHeap.extractMin() 
			u = newHeapNode[0] 
			for pCrawl in self.graph[u]: 

				v = pCrawl[0] 

				if minHeap.isInMinHeap(v) and dist[u] != int(1e10) and pCrawl[1] + dist[u] < dist[v]: 
						dist[v] = pCrawl[1] + dist[u] 
						minHeap.decreaseKey(v, dist[v]) 

		return dist


def driver(k,x,g,n):
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
    k=10
    x = 3000
    g = Graph(n)
    for i in range(len(a)):
        g.addEdge(a[i],b[i],w[i])
    print(driver(k,x,g,n))
input()