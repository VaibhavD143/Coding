class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        if len(A)<2:
            return 0
        # dp = [float('inf')]*(len(A))
        # dp[0] = 0
        
        # assigned =0   #last assigned index, that's minimum for sure
        # for i in range(len(A)):
        #     #if this touhes the last index
        #     if i+A[i]>=len(A)-1:
        #         return dp[i]+1 if dp[i] != float('inf') else -1
            
        #     for j in range(assigned+1,i+A[i]+1):
        #         if j>=len(A):
        #             break
        #         dp[j] = min(dp[j],1+dp[i])
        #         assigned = j
            
        # return dp[-1] if dp[-1] != float("inf") else -1
        
        reach = 0
        next_reach = 0
        i=0
        steps =0
        while i<len(A):
            if i>reach:
                reach = next_reach
                steps+=1
                if reach<i:
                    return -1
                if reach>=len(A)-1:
                    break
            next_reach = max(next_reach,i+A[i])
            i+=1
        return steps
        
        