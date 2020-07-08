"""
Intution:
Standard MST problem, applying krushkal's and for cycle checking using disjoint set!
"""
import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        disjoint =list(range(A))
        def assign(i,parent):
            disjoint[findParent(i)]=findParent(parent)
        
        def findParent(i):
            if i != disjoint[i]:
                disjoint[i]=findParent(disjoint[i])
            return disjoint[i]
    
        ha=[]
        for edge in B:
            heapq.heappush(ha,list(reversed(edge)))
        del B
        cnt=A-1
        cost=0
        while cnt:
            edge = heapq.heappop(ha)
            if findParent(edge[1]-1) != findParent(edge[2]-1):
                cost+=edge[0]
                assign(edge[1]-1,edge[2]-1)
                cnt-=1
            
        return cost
            
            
            
        