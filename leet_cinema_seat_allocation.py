class Solution:
    def maxNumberOfFamilies(self, n: int, r: List[List[int]]) -> int:
        r.sort()
        res=n*2
        ind=0
        prev = r[ind][0]
#         while ind<len(r):
#             lst = set()
            
#             while ind<len(r) and r[ind][0]==prev:
#                 lst.add(r[ind][1])
#                 ind+=1
                
#             if len(lst.intersection(set([2,3,4,5]))) == 0:
                
#                 if len(lst.intersection(set([6,7,8,9]))) == 0:
#                     pass
#                 else:
#                     res-=1
#             elif len(lst.intersection(set([6,7,4,5]))) == 0:
#                 res-=1
#             elif len(lst.intersection(set([6,7,8,9]))) == 0:
#                 res-=1
#             else:
#                 res-=2
            
#             prev = r[ind][0] if ind<len(r) else None
#         return res
        left = (1<<1)|(1<<2)|(1<<3)|(1<<4)
        center = (1<<3)|(1<<4)|(1<<5)|(1<<6)
        right = (1<<5)|(1<<6)|(1<<7)|(1<<8)
        
        while ind<len(r):
            row = 0

            while ind<len(r) and r[ind][0]==prev:
                row|=(1<<(r[ind][1]-1))
                ind+=1

            if row&left == 0:
                if row&right != 0:
                    res-=1
            elif row&right == 0:
                res-=1
            elif row&center == 0:
                res-=1
            else:
                res-=2
            prev = r[ind][0] if ind<len(r) else None
        return res
                