class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for i in range(1,2*n,2):
            res *= (i*(i+1))//2 
            res%=1000000007
        return res