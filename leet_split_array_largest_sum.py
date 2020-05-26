"""
Intution:
We are doing binary search on max number `n` and condition we are using is:
if it is possible to divide into `mid` parts which are less than or equal to `m` with max sum not greater than `n`. 
less than 'm' allowed as we are not finalising as answer 
https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation
"""
class Solution:
    def splitArray(self, lst: List[int], m: int) -> int:
        if m>len(lst):
            return -1
        if m==len(lst):
            return max(lst)
        
        def isValid(n,A,B):
            curr=0
            st=0
            for i in A:
                curr+=i
                if curr>n:
                    curr=i
                    st+=1
            
            return st+1<=B
        
        low=max(lst)
        high=sum(lst)
        while low<=high:
            mid = low+(high-low)//2
            
            if isValid(mid,lst,m):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
#Old#Dp
lst = [7,2,5,10,8]
m = 4
def pp(matrix):
    for row in matrix:
        print(row)
dp = [[0]*len(lst) for _ in range(m)]
dp[0][-1] = lst[-1]

#Postfix sum, use in final last computation
for i in range(len(lst)-2,-1,-1):
    dp[0][i] = dp[0][i+1]+lst[i]
#Prefix sum
for i in range(1,len(lst)):
    dp[1][i] = dp[1][i-1]+lst[i-1]

#dp[i][j] : max sum from all parts where array is divided into `i` parts till index j
#that's why dp[1][j] = prefix sum till j, it is stating single partition

#for each partition
for i in range(2,m):
    #starting from i, as it is least possible index for total I partitions
    # going till len(lst)-(m-i-1), leaving indexes for remaining partitions
    for j in range(i,len(lst)-(m-i-1)):
            minVal = float('inf')
            #trying to create ith partition from possible least index and to most index
            #dp[i-1][k]: i-1 partition till index k and next partition between k&j (sum(lst[k:j+1]))
            for k in range(i-1,j):
                minVal = min(minVal,max(dp[i-1][k],dp[1][j]-dp[1][k]))
            dp[i][j] = minVal
res = float('inf')
#finding result for mth partition, where we get least answer
for i in range(m-1,len(lst)):
    res = min(res,max(dp[0][i],dp[m-1][i]))
print(res)