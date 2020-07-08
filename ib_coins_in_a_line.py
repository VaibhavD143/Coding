"""
Intution:
dp[start][end] : it stores profit one will make between index start,end both inclusive taking first chance
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        def bestChoice(start,end):
            if start == end:
                return A[start]
            
            # if end-start == 1:
            #     return max(A[start],A[end])
            
            if dp[start][end] != -1:
                return dp[start][end]
                # if mine:
                #     return dp[start][end]
                # else:
                #     return (pref[end+1]-pref[start])-dp[start][end]
            
            #if selects A[start] then remaining array will return max profit of opponent, so deducting it from total sum will give us our profit from remaining array
            l = A[start] + (pref[end+1]-pref[start+1])-bestChoice(start+1,end)
            r = A[end] + (pref[end]-pref[start]) - bestChoice(start,end-1)
            
            dp[start][end] = max(l,r)
            return dp[start][end]
            # if mine:
            #     return dp[start][end]
            # else:
            #     return (pref[end+1]-pref[start])-dp[start][end]
        
        dp = [[-1]*len(A) for _ in range(len(A))]
        pref = [0]
        for i in A:
            pref.append(pref[-1]+i)
        return bestChoice(0,len(A)-1)