"""
Gyaan:
graph banalo
"""
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not len(A) or not len(B):
            return []
        
        res=[]
        ia,ib=0,0
        while ia<len(A) and ib<len(B):
            curr=[max(A[ia][0],B[ib][0]),min(A[ia][1],B[ib][1])]
            if curr[0]<=curr[1]:
                res.append(curr)
            if curr[1] == A[ia][1]:
                ia+=1
            else:
                ib+=1
                
        return res
        