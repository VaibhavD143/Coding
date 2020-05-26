class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, lst, k):
        cur=0
        res=0
        l,rl=0,0
        r,rr=0,0
        n=k
        while r<len(lst):
            if lst[r]==1:
                cur+=1
                r+=1
            elif n:
                n-=1
                cur+=1
                r+=1
            #to handle case when n = 0 so it won't get stuck in a loop
            elif l ==r:
                r+=1
                l+=1
            else:
                while l<r and n==0:
                    if lst[l]==1:
                        cur-=1
                        l+=1
                    else:
                        cur-=1
                        n+=1
                        l+=1
            if res<cur:
                rl=l
                rr=r
                res=cur
        return list(range(rl,rr))