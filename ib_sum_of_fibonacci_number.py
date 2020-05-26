from bisect import bisect_right,bisect_left
class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        fib=[1,1]
        while fib[-1]+fib[-2]<=A:
            n=fib[-1]+fib[-2]
            fib.append(n)
        
        num = A-fib[-1]
        res=1
        while num:
            ind = bisect_left(fib,num)
            if num == fib[ind]:
                res+=1
                break
            num-=fib[ind-1]
            res+=1
        return res