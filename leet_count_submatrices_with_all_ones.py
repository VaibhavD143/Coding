"""
Intution:
https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720265/Java-Detailed-Explanation-From-O(MNM)-to-O(MN)-by-using-Stack
Version 1:
Take all possible combinations of columns and make it an 1D array, now counting for 1D array is pretty easy
Version 2:
sm[i] : possible matrices ending with ith column
sm[i] = sm[ss[-1]] #all the mattrices possible with height lesser than arr[i]
sm[i] += (i-ss[-1])*arr[i] #matrices till index where height is greater or equal than arr[i]
"""
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # def getCount(arr):
        #     res,length =0,0 
        #     for i in range(len(arr)):
        #         length= 0 if arr[i]==0 else length+1
        #         res+=length
        #     return res
        # res=0
        # for r1 in range(len(mat)):
        #     arr = mat[r1][:]
        #     for r2 in range(r1,len(mat)):
        #         for i in range(len(mat[0])):
        #             arr[i]&=mat[r2][i]
        #         res+=getCount(arr)
        # return res
        res =0
        arr = [0]*len(mat[0])
        for r in range(len(mat)):
            for i in range(len(mat[0])):
                arr[i] = arr[i]+1 if mat[r][i]==1 else 0
            ss = []
            sm = [0]*len(arr)
            for i in range(len(mat[0])):
                
                while ss and arr[ss[-1]]>=arr[i]:
                    ss.pop()
                
                if ss:
                    sm[i]=sm[ss[-1]]
                    sm[i]+=(i-ss[-1])*arr[i]
                else:
                    sm[i]=(i+1)*arr[i]
                res+=sm[i]
                ss.append(i)
        return res