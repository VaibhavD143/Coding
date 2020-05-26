"""
Intution:
We are doing binary search on max number `mid` and condition we are using is:
if it is possible to divide into `st+1` parts which are less than or equal to `B` with max sum not greater than `mid`. 
less than 'B' allowed as we are not finalising as answer 
https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if B>len(A):
            return -1
        if B==len(A):
            return max(A)
        
        def isValid(n,A,B):
            curr=0
            st=0
            for i in A:
                curr+=i
                if curr>n:
                    curr=i
                    st+=1
            
            return st+1<=B
        
        low=max(A)
        high=sum(A)
        while low<=high:
            mid = low+(high-low)//2
            
            if isValid(mid,A,B):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    
        # dp=[[-1]*len(A) for _ in range(B) ]
        # pref = [0]
        # for i in A:
        #     pref.append(pref[-1]+i)
        
        # def partInK(ind,k,pref,dp):
        #     # print(ind,k)
        #     if dp[k][ind]!=-1:
        #         return dp[k][ind]
        #     if k==0:
        #         return pref[-1]-pref[ind]
        #     res = float('inf')
        #     for i in range(ind+1,len(pref)-k):
        #         res = min(res,max(pref[i]-pref[ind],partInK(i,k-1,pref,dp)))
        #     dp[k][ind] = res
        #     return res
            
        # return partInK(0,B-1,pref,dp)