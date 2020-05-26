"""
Intution:
- Considering current element as geater so for that getting number considering value and index such that it can give max value for f(i,j).
Same but considering current element lesser and getting greater elemnt such that it gives max f(i,j) for that index.
- Here calc is the constrain we are using to replace min value and max value currently available.
- If f(i,j) where j is index of current element and i is minValue as per the calculation then f(j,i) will be considered in max case.
EDITORIAL is LIT!
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        cmin = A[0]
        mind = 0
        calc = A[0]
        res = 0
        for i in range(1,len(A)):
            if A[i]>=cmin:
                res = max(res,abs(A[i]-cmin)+abs(i-mind))
            elif A[i]+i<calc:
                cmin=A[i]
                mind=i
                calc=A[i]+i
        # print(res)
        cmax = A[0]
        maxd = 0
        calc = A[0]
        for i in range(1,len(A)):
            if A[i]<=cmax:
                res = max(res,abs(A[i]-cmax)+abs(i-maxd))
                # print(res,A[i],cmax,i,maxd)
            elif A[i]-i>calc:
                cmax=A[i]
                maxd=i
                calc=A[i]-i
        return res
# EDITORIAL
def maxArr(self, a):
    n = len(a)
    ap = [a[i] + i for i in range(n)]
    am = [a[i] - i for i in range(n)]
    return max(max(ap) - min(ap), max(am) - min(am))
