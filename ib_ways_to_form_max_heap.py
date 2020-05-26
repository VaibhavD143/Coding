"""
Gyaan:
comb could be:
def binomialCoefficient(n, k): 
  
    # since C(n, k) = C(n, n - k) 
    if (k > n - k): 
        k = n - k 
  
    # initialize result 
    res = 1
  
    # Calculate value of [n * (n-1) *---* (n-k + 1)] 
    # / [k * (k-1) *----* 1] 
    for i in range(k): 
        res = res * (n - i) 
        res = res / (i + 1) 
    return res 
"""
import math
class Solution:
    
    def __init__(self):
        self.fact=[1]

    def facto(self,n):
        if len(self.fact)>n:
            return self.fact[n]
        while len(self.fact)<=n:
            self.fact.append(self.fact[-1]*(len(self.fact)))
        return self.fact[n]

    def comb(self,n,r):
        if n<r:
            return 0
        r = min(r,n-r)
        return self.facto(n)//(self.facto(n-r)*self.facto(r))

    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:
            return 1
        if A == 2:
            return 1
        if A == 3:
            return 2
        h = 1+int(math.log2(A))
        lastLevel = 2**(h-1)
        rem = A-lastLevel+1
        left = min(rem,lastLevel//2)    #node in left part in last level
        left = left+(lastLevel-2)//2    #node in left side of the root
        return (self.comb(A-1,left)*self.solve(left)*self.solve(A-1-left))%1000000007