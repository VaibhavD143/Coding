class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        # sm = sum(A)
        # smgap = (len(A)*(len(A)+1))//2 - sm
        # nsm = sum(map(lambda i:i**2,A))
        # sqgap = sum(map(lambda i:i**2,range(1,len(A)+1)))-nsm
        # mPr = sqgap//smgap
        # m = (mPr+smgap)//2
        # r = mPr - m
        # return [r,m]
        sm =0
        squar_sm = 0
        for i,val in enumerate(A):
            sm+=(i+1)
            sm-=val
            squar_sm += (i+1)**2
            squar_sm -= val**2
        #m:missing, r:repeating
        mSr = sm
        mPr = squar_sm//sm
        m = (mSr+mPr)//2
        r = mPr-m
        return [r,m]
        