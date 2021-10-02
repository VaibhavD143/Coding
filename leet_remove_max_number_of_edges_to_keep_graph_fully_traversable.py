"""
Intution:
we are finding MST for both of them and rest edges are answer
first we take all the edges which are common to them because single edge is working for both
once we are done with common edges, we start with individual edge.
"""
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        def union(parent,i1,i2):
            p1 = find(parent,i1)
            p2 = find(parent,i2)
            
            if p1==p2:
                return False
            
            parent[p1] = p2
            return True
        
        def find(parent,i):
            if i!=parent[i]:
                parent[i] = find(parent,parent[i])
            return parent[i]
        
        edges.sort(reverse=True)
        par= list(range(n))
        cnt = n-1
        ans = i = 0
        while i<len(edges) and edges[i][0]==3:
            if union(par,edges[i][1]-1,edges[i][2]-1):
                cnt-=1
            else:
                ans+=1 
            i+=1
        cnt1 = cnt
        cnt2 = cnt
        par1 = par
        par2 = par[:]
        while i<len(edges) and edges[i][0] == 2:
            if union(par2,edges[i][1]-1,edges[i][2]-1):
                cnt1-=1
            else:
                ans+=1
            i+=1
        while i<len(edges) and edges[i][0] == 1:
            if union(par1,edges[i][1]-1,edges[i][2]-1):
                cnt2-=1
            else:
                ans+=1
            i+=1
        if cnt1 ==0 and cnt2 ==0:
            return ans
        return -1
            
        