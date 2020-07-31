"""
Can't have memorization as 
Ex:
a b c e
s f e s
string "cesef"
at `s` if i visit from 'e'(1,2) then dp[1,3] will become False but if we visit 's' from [0,3] then answer is possible!
"""
class Solution:
    def exist(self, A: List[List[str]], B: str) -> bool:
        def dfs(i,j,k):
            if k ==0:
                return 1
            # if (i,j,k) in ha:
            #     return ha[(i,j,k)]
            if i<0 or i>=len(A) or j<0 or j>=len(A[0]):
                return 0
            if B[-k] == A[i][j]:
                # print(i,j,k,A[i][j])
                A[i][j] = '#'
                res = dfs(i+1,j,k-1) or dfs(i-1,j,k-1) or dfs(i,j-1,k-1) or dfs(i,j+1,k-1)
                A[i][j] = B[-k]
                # print(ha[(i,j,k)])
                return res
            # ha[i,j,k] = 0
            return 0
        
        if not B:
            return 1
        if not A:
            return 0
        # for r in A:
        #     print(r)
        # ha={}
        # print(dfs(0,4,len(B)))
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == B[0]:
                    # print(i,j)
                    if dfs(i,j,len(B)):
                        return 1
        return 0