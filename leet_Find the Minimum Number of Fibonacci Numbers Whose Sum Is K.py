import bisect
class Solution:
    def findMinFibonacciNumbers1(self, k: int) -> int:
        fib = [1,1]
        while fib[-1]<k:
            fib.append(fib[-1]+fib[-2])
        res=0
        while k:
            ind = bisect.bisect(fib,k)
            if ind==len(fib) or fib[ind]!=k:
                res+=1
                k-=fib[ind-1]
            else:
                return res+1
        return res
    def findMinFibonacciNumbers(self, k):
        if k < 2: return k
        a, b = 1, 1
        while b <= k:
            a, b = b, a + b
        return self.findMinFibonacciNumbers(k - a) + 1