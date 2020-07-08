"""
Intution:
Convert problem into 1-D array sum no larger than k
How?:
prefix sum of each row, take pair of each columns possible N^2
"""
import bisect
class Solution:
    def maxSumSubmatrix(self, mat: List[List[int]], k: int) -> int:
        if not mat or not mat[0]:
            return 0
        #Finding max subarray sum no larger than K in given arr
        def findSum(arr,k):
            res = -1000000000
            pref = [0]
            curr = 0
            for i in range(len(arr)):
                curr+=arr[i]
                diff = curr-k-1
                ind = bisect.bisect(pref,diff)
                if ind != len(pref):
                    res = max(res,curr-pref[ind])
                bisect.insort(pref,curr)
            return res
        #For prefix sum in columns and pair of rows, but case had rows way greater than columns. To avoid TLE
        # for i in range(1,len(mat)):
        #     for j in range(len(mat[0])):
        #         mat[i][j]+=mat[i-1][j]
        
        #prefix sum in rows
        for i in range(len(mat)):
            for j in range(1,len(mat[0])):
                mat[i][j]+=mat[i][j-1]
        #minimum answer if sum is not possible
        res= -1000000000
        #each pair of row
        # for i1 in range(len(mat)):
        #     for i2 in range(i1,len(mat)):
        #         arr = [mat[i2][j]-(mat[i1-1][j] if i1!=0 else 0) for j in range(len(mat[0]))]
        #         res = max(res,findSum(arr,k))
        
        #each pair of column
        for j1 in range(len(mat[0])):
            for j2 in range(j1,len(mat[0])):
                #if c1=2 and c2=4 then we need sum between 2 and 4 so will delete sum of c=1 from c2=4 which will give sum from 2 to 4
                arr = [mat[i][j2]-(mat[i][j1-1] if j1!=0 else 0) for i in range(len(mat))]
                res = max(res,findSum(arr,k))
        
        
        return res