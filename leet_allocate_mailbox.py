"""
Intution:
Trying clustering into k groups and finding minimum cost
catcch: we put mail box to median house
why?
if n=1: then on the house
if n=2[a,b]: then any where between a,b
if n=3 [a,b,c] : on 'b', because point is x, ax+xc is static as long as it is between [a,c]. to minimise we are supposed to minimise distance from b that is on 'b'
if n=4[a,b,c,d]: then in-between [a,d] and [c,d]
"""
class Solution:
    def minDistance(self, h: List[int], k: int) -> int:
        
        def cost(l,r):
            if (l,r) in c:
                return c[l,r]
            med = h[(l+r)//2]
            d = 0
            for i in range(l,r+1):
                d+=abs(h[i]-med)
            c[l,r]=d
            return d

        
#         def rec(ind,k):
#             if ind == len(h):
#                 if k==0:
#                     return 0
#                 else:
#                     return float('inf')
#             if k==1:
#                 return cost(ind,len(h)-1)
            
#             if (ind,k) in ha:
#                 return ha[ind,k]
#             d=float('inf')
#             for i in range(ind,len(h)):
#                 d=min(d,cost(ind,i)+rec(i+1,k-1))
#             ha[ind,k] = d
#             return d
        
        h.sort()
        # dp=[[None]*(k+1) for _ in range(len(h))]
        c={}
        # ha={}
        # return rec(0,k)
        ha = [[float('inf')]*(k+1) for _ in range(len(h))]
        for i in range(len(h)):
            ha[i][1]=cost(i,len(h)-1)
            
        for k in range(2,k+1):
            for i in range(len(h)):
                d=float('inf')
                for j in range(i,len(h)-k+1):
                    d = min(d,cost(i,j)+ha[j+1][k-1])
                ha[i][k] = d
        return ha[0][-1]
#         def rec(l,r,k):
#             if k==0:
#                 return float('inf')
#             if l==r:
#                 if k==1:
#                     return 0
#                 else:
#                     float('inf')
#             if k == 1:
#                 median = h[(r+l)//2]

#                 d=0
#                 for i in range(l,r+1):
#                     d+=abs(h[i]-median)
#                 return d
                
#             if (l,r,k) in ha:
#                 return ha[l,r,k]
#             d = float('inf')
#             for i in range(l,r):
#                 td = rec(l,i,1)+rec(i+1,r,k-1)
#                 d = min(d,td)
#             ha[l,r,k] = d
#             return d
#         h.sort()
#         ha={}
#         return rec(0,len(h)-1,k)
    