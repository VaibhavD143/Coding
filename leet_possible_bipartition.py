def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        def bfs(ind):
            curr,assign=1,2
            ss = deque([ind,None])
            visited[ind] = curr
            while ss:
                node = ss.popleft()
                #current level completed
				if node == None:
                    #if there no other nodes left. two-colored graph possible. Return True
					if not len(ss):
                        return True
					#Swap color as level changed,append None at the end again.
                    curr,assign = assign,curr
                    ss.append(None)
                
                for v in graph[node]:
                    if visited[v] == curr:
                        return False
                    elif visited[v] == 0:
                        visited[v]=assign
                        ss.append(v)
            #will never reach here
			# return True
            
        
        
        graph = defaultdict(list)

        for edge in dislikes:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        visited = [0]*(N+1)
        for i in range(1,N+1):
			#To consider disconnected graph in BFS
            if visited[i] == 0:
                if not bfs(i):
                    return False
        return True