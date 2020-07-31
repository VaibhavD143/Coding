"""
Intution:
l1 is left-most valid index for substring ending at rth index
l2 is left-most index from where substring becomes invalid ending at rth index
so we can generate l2-l1 substrings ending at rth index
Valid : have exactly K distinct elements
 
"""
from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, lst: List[int], K: int) -> int:
        
        l1 = l2 = res = 0
        dist1 = dist2 = 0
        ha1 = {}
        ha2 = {}
        for r in range(len(lst)):
            
            if ha1.get(lst[r],0) == 0:
                dist1+=1
            if ha2.get(lst[r],0) == 0:
                dist2+=1
            ha1[lst[r]] = ha1.get(lst[r],0)+1
            ha2[lst[r]] = ha2.get(lst[r],0)+1
            while dist1>K:
                ha1[lst[l1]] -=1
                if ha1[lst[l1]] == 0:
                    dist1-=1
                l1+=1
            while dist2>=K:
                ha2[lst[l2]] -=1
                if ha2[lst[l2]] == 0:
                    dist2-=1
                l2+=1
            res+=l2-l1
        return res
    
        # return self.atMostK(A,K)-self.atMostK(A,K-1)
        
    def atMostK(self,lst,k):
        l = res = 0
        ha = defaultdict(int)
        dist = 0
        for r in range(len(lst)):
            
            if ha[lst[r]] == 0:
                dist+=1
            ha[lst[r]]+=1
            while dist>k:
                ha[lst[l]]-=1
                if ha[lst[l]] == 0:
                    dist-=1
                l+=1
            
            res+= r-l+1
        return res