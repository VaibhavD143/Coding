from bisect import bisect_left
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        lst = []
        for i,val in enumerate(A):
            lst.append([val,i])
        lst.sort()
        #after sorting it becomes problem of keeping record of smallest on left side
        cmin=lst[0][1]
        res=0
        for elem in lst:
            res=max(res,elem[1]-cmin)
            cmin = min(cmin,elem[1])
        return res
            
        # ss=[]
        # ssi=[]
        # cur=0
        # for i,val in enumerate(A):
        #     if not ss:
        #         ss.append(A[i])
        #         ssi.append(i)
        #     elif ss[-1]>val:
        #         ss.append(val)
        #         ssi.append(i)
        #     # print(ss,'---------')
        #     ind = bisect_left(ss[::-1],val)
        #     # print(ind)
        #     if ind == len(ss):
        #         ind=0
        #     elif ss[len(ss)-1-ind]==val:
        #         ind = len(ss)-1-ind
        #     else:
        #         ind = len(ss)-1-(ind-1)
        #     # print(ind,i,ssi[ind])
        #     cur=max(cur,i-ssi[ind])
        # return cur if cur else -1