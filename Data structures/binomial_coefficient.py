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
obj = Solution()
print(obj.comb(5,4))
print(binomialCoefficient(5,4))