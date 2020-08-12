"""
Intution:
find divisor of each element and if divisor is already occupied by another element then union both elements
otherwise occupy this divisor for this element
keeping hashtable for keeping record of index of first element who is occupying that divisor key:divisor val:index of element
"""
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        
        def union(i1,i2):
            p1 = find(i1)
            p2 = find(i2)
            
            if p1 == p2:
                return
            if rank[p1]>rank[p2]:
                p1,p2 = p2,p1
            
            parent[p1] = p2
            rank[p2]+=1
        
        def find(i1):
            if parent[i1] != i1:
                parent[i1] = find(parent[i1])
            return parent[i1]
        
        parent = list(range(len(A)))
        rank = [0]*len(A)
        ha = {}
        
        for i,n in enumerate(A):
            for p in range(2,1+int(math.sqrt(n))):
                if n%p == 0:
                    if p not in ha:
                        ha[p] = i
                    else:
                        union(ha[p],i)
                    other = n//p
                    if other not in ha:
                        ha[other] = i
                    else:
                        union(ha[other],i)
            if n not in ha:
                ha[n] = i
            else:
                union(ha[n],i)
        
        for i in range(len(A)):
            find(i)
        cnt = Counter(parent)
        return max(cnt.values())