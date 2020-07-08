class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        ha = {}
        def rec(n):
            if n==1:
                return 0
            if n in ha:
                return ha[n]
            
            if n&1:
                ha[n] =  1+(rec(n*3+1))
            else:
                ha[n] = 1+rec(n//2)
            return ha[n]
        # print(rec(12))
        pw = []
        for i in range(lo,hi+1):
            pw.append([rec(i),i])
        pw.sort()
        return pw[k-1][1]
        