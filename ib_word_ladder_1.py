from collections import deque
class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer
    def solve(self, A, B, C):
        # # print(A,B,C)
        nodes = list(set([A]+C+[B]))
        nodes = [A]+C+[B]
        # def isEdge(s1,s2):
        #     flag=True
        #     for i,j in zip(s1,s2):
        #         if i!=j:
        #             if not flag :
        #                 return False
        #             flag = False
        #     return True
        # # print(C)
        # # print(nodes)
        # graph=[[] for _ in range(len(nodes))]
        
        # for i in range(len(nodes)):
        #     for j in range(i+1,len(nodes)):
        #         if isEdge(nodes[i],nodes[j]):
        #             graph[i].append(j)
        #             graph[j].append(i)
        # print(graph)
        ha={}
        graph=[[] for _ in range(len(nodes))]
        for ind,word in enumerate(nodes):
            for i in range(len(A)):
                tmp = word[:i]+'_'+word[i+1:]
                if tmp in ha:
                    ha[tmp].append(ind)
                else:
                    ha[tmp] = [ind]
        
        for _,vals in ha.items():
            for i in range(len(vals)):
                for j in range(i+1,len(vals)):
                    graph[vals[i]].append(vals[j])
                    graph[vals[j]].append(vals[i])
        
        visited = [False]*len(nodes)
        ss = deque([0,None])
        dist = 1
        while ss:
            u=ss.popleft()
            if u == None:
                if not len(ss):
                    break
                ss.append(None)
                dist+=1
                continue
            for v in graph[u]:
                if not visited[v]:
                    visited[v]=dist
                    ss.append(v)
        return visited[-1]+1 if visited[-1] else 0