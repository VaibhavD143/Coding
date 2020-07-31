class Solution:
    def permuteUnique(self, A: List[int]) -> List[List[int]]:
        def rec(A,lst,used):
            if len(lst) == len(A):
                res.append(lst[:])
                return
            
            for i in range(len(A)):
                if used[i]:
                    continue
                if i>0 and A[i] == A[i-1] and not used[i-1]:
                    continue
                used[i] = True
                lst.append(A[i])
                rec(A,lst,used)
                lst.pop()
                used[i] = False
            
            
    
        used = [False]*len(A)
        res = []
        A.sort()
        rec(A,[],used)
        return res