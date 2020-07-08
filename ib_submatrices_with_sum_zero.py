"""
Intution:
calculating prefix sum  matrix in-place
for every pair of rows, we are calculating as subarray with sum `0`,
i.e:
mat = 0|  1  2  3   => 0|  1  3  6
      1|  4  5  6      1|  5 12 21
      2|  7  8 -6      2| 12 27 30
    for r1 = 1 and r2 =2
    so mat[r2][1]-mat[r1-1][1] = 23 and mat[r2][2]-mat[r1-1][2] =23(column matrix)

"""
from collections import defaultdict
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A or not A[0]:
            return 0
        res=0
        
        for j in range(1,len(A[0])):
            A[0][j] += A[0][j-1]
            
        for i in range(1,len(A)):
            A[i][0]+=A[i-1][0]
            
        for i in range(1,len(A)):
            for j in range(1,len(A[0])):
                A[i][j] +=A[i-1][j]+A[i][j-1]-A[i-1][j-1]
                
        for i in range(1):
            for j in range(len(A)):
                r1=i
                r2=j
                ha=defaultdict(int)
                ha[0]=1
                for k in range(len(A[0])):
                    sm = A[r2][k]
                    res+=ha[sm]
                    ha[sm]+=1
                
        # print(res)
        for i in range(1,len(A)):
            for j in range(i,len(A)):
                r1 = i
                r2 = j
                ha=defaultdict(int)
                ha[0]=1
                for k in range(len(A[0])):
                    sm = A[r2][k]-A[r1-1][k]
                    res+=ha[sm]
                    ha[sm]+=1
                    # print(res,k,sm)
        # for r in A:
        #     print(r)
        return res
        
                