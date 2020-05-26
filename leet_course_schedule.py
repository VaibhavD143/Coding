class Solution:
    def canFinish(self, num, prerequisites):
        def isCyclicUtil( v, graph,visited, recStack): 
            visited[v] = True
            recStack[v] = True

            for neighbour in graph[v]: 
                if visited[neighbour] == False: 
                    if isCyclicUtil(neighbour, graph, visited, recStack) == True: 
                        return True
                elif recStack[neighbour] == True: 
                    return True
            recStack[v] = False
            return False

        def isCyclic(graph): 
            visited = [False] * len(graph) 
            recStack = [False] * len(graph) 
            for node in range(len(graph)): 
                if visited[node] == False: 
                    if isCyclicUtil(node,graph,visited,recStack) == True: 

                        return True
            return False
        # if num<2:
        #     return True
        graph = [[] for _ in range(num)]
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
        # print(graph)
        return isCyclic                