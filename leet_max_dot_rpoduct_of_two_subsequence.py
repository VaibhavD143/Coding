"""
Intution:
classic take it not take it problem!
"""
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
#         def fun(lst1,lst2,ind1,ind2,prod):
#             # print(ind1,ind2,prod)
#             if len(lst1)==ind1 or len(lst2)==ind2:
#                 # dp[ind1][ind2]=prod
#                 return prod
            
#             if dp[ind1][ind2]!=-1:
#                 return dp[ind1][ind2]+prod
            
#             dp[ind1][ind2]=max(fun(lst1,lst2,ind1+1,ind2,0),fun(lst1,lst2,ind1,ind2+1,0),fun(lst1,lst2,ind1+1,ind2+1,0),fun(lst1,lst2,ind1+1,ind2+1,lst1[ind1]*lst2[ind2]))
            
#             return dp[ind1][ind2]+prod
            
        #Handaling -ve answers
        def fun(lst1,lst2,ind1,ind2):
            if len(lst1)==ind1 or len(lst2)==ind2:
                return float('-inf')
            
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            
            dp[ind1][ind2]=max(fun(lst1,lst2,ind1+1,ind2),fun(lst1,lst2,ind1,ind2+1),fun(lst1,lst2,ind1+1,ind2+1),max(fun(lst1,lst2,ind1+1,ind2+1),0)+lst1[ind1]*lst2[ind2])
            
            return dp[ind1][ind2]
            
            
            
        dp=[[-1]*(len(nums2)) for _ in range(len(nums1))]
        fun(nums1,nums2,0,0)
        # for r in dp:
        #     print(r)
        return dp[0][0]