class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        def run(lst,rem,res):
            if not rem:
                res.append(lst[:])
            for i in range(len(rem)):
                lst.append(rem[i])
                run(lst,rem[:i]+rem[i+1:],res)
                lst.pop()
        lst=[]
        rem = A
        res=[]
        run(lst,rem,res)
        return res