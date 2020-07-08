from collections import defaultdict
class Solution:
    # @param A : string
    # @return an integer
    def anytwo(self, A):
        # ha = defaultdict(list)
        # for i,val in enumerate(A):
        #     ha[val].append(i)
        
        # for key,val in ha.items():
        #     if len(val)<2:
        #         continue
            
        #     for key2,val2 in ha.items():
        #         if len(val2)<2:
        #             continue
        #         if key == key2:
        #             if len(val2)>2:
        #                 return 1
        #             else:
        #                 continue
        #         if val[0]<val2[-2] and val[1]<val2[-1]:
        #             return 1
        # return 0
        # dp = [[0]*(len(A)+1) for _ in range(len(A)+1)]
        
        # for i in range(1,len(A)+1):
        #     for j in range(1,len(A)+1):
        #         if i!=j and A[i-1]==A[j-1]:
        #             dp[i][j] = dp[i-1][j-1]+1
        #         else:
        #             dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        # return 1 if max(map(max,dp))>=2 else 0
        """
        Intution : We only care about subsequence of length 2,
        case1: abab
        case2: aabb
        case3: aaa
        """
        seen = set()
        #this will find first repetation of any character
        i=0
        while i <len(A):
            if A[i] in seen:
                break
            seen.add(A[i])
            i+=1
        #if no character gets repeated at all
        if i == len(A):
            return 0
        #this will remove all the characters occured before first occurence of our repeated character, including out 
        j=0
        while A[j]!=A[i]:
            # print(j,A[j])
            seen.remove(A[j])
            j+=1
        for j in range(i+1,len(A)):
            if A[j] in seen:
                return 1
            seen.add(A[j])
        return 0
