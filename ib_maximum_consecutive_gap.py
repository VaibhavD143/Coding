"""
Intution: Editorial
"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if not A or len(A)==1:
            return 0
        if len(A) ==2:
            return max(A)-min(A)
        minn = min(A)
        maxn = max(A)
        gap = (maxn-minn)/(len(A)-1)
        if gap == 0:
            return 0
        min_buc = [float('inf')]*(len(A))
        max_buc = [float('-inf')]*(len(A))
        for i in A:
            ind = int((i-minn)//gap)
            # print(ind,i,minn,gap)
            min_buc[ind] = min(min_buc[ind],i)
            max_buc[ind] = max(max_buc[ind],i)
        diff=0
        l,r=0,1
        while r<len(A):
            while r<len(A) and min_buc[r] == float('inf'):
                r+=1
            if r==len(A):
                break
            diff = max(diff,min_buc[r]-max_buc[l])
            l=r
            r+=1
        return diff