class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def arrange(self, A, B):
        prefW = [0]
        prefB = [0]
        for i in A:
            if i =='W':
                prefW.append(prefW[-1]+1)
                prefB.append(prefB[-1])
            else:
                prefW.append(prefW[-1])
                prefB.append(prefB[-1]+1)
        
        #dp[i][j] : divide array with i cuts, i=1 : divide array into 2 parts with 1 cut. Till jth column(inclusive).. Stores minimum sum possible
        #dp[1][-1] : consider whole array with 1 cut have minimum sum

        dp= [[-1]*len(A) for _ in range(B)]
        
        for i in range(len(A)):
            dp[0][i] = prefW[i+1]*prefB[i+1]
        
        #if there is cuts more than 0 OR parts more than 1
        for i in range(1,B):
            #non-empty partitions, so starting from i and leaving end indices for remaining partitions
            for j in range(i,len(A)-(B-i-1)):
                #considering all posibility here i:k-1 and k:j (both inclusive). if 1:1 then only element at 1
                res= float('inf')
                for k in range(i,j+1):
                    #j+1, as prefix is storing sum 1-based index
                    addW = prefW[j+1]-prefW[k]
                    addB = prefB[j+1]-prefB[k]
                    add = addW*addB
                    res = min(res,dp[i-1][k-1]+add)
                dp[i][j]=res
        # for r in dp:
        #     print r
        return dp[-1][-1]