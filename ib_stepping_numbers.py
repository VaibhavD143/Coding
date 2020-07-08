class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        def add(n):
            nonlocal A
            nonlocal B
            if n>B:
                return
            if A<=n<=B:
                res.append(n)
            last = n%10
            if last==0:
                add(n*10+last+1)
            elif last == 9:
                add(n*10+last-1)
            else:
                add(n*10+last-1)
                add(n*10+last+1)
        res=[]
        if A<=0:
            res.append(0)
        for i in range(1,10):
            add(i)
        res.sort()
        return res