class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        # sat.sort()
        # ind=0
        # while ind<len(sat) and sat[ind]<0:
        #     ind+=1
        # res = 0
        # sm=0
        # for i in range(ind,len(sat)):
        #     res+=(i-ind+1)*sat[i]
        #     sm+=sat[i]
        # ind-=1  #greatest negative
        # while ind>=0:
        #     sm+=sat[ind]
        #     if sm<0:
        #         break
        #     res+=sm
        #     ind-=1
        # return res
        
        sat.sort()
        res = 0
        sm = 0
        while sat and sat[-1]+sm>0:
            sm+=sat.pop()
            res+=sm
        return res