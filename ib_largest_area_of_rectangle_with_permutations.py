"""
Intution:
keeping columns having maximum consecutive 1's in column manner,right most side
ex.
0 1 2 3
-------
1 0 1 1 (config = 1 0 2 3)
1 1 0 1 (config = 2 1 0 3)
"""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        config = list(range(len(A[0]))) #current configureation of columns for current row index, stores inex of columns
        maxArea = 0
        for i in range(len(A)):
            slow = 0    #at which place it needs to be added
            fast = 0
            while fast<len(A[0]):
                if A[i][config[fast]] == 0:
                    col = config[fast]
                    config.pop(fast)
                    config.insert(slow,col)
                    slow+=1
                fast+=1
            j=0
            tmpI=i
            # print(config)
            while j<len(A[0]) and tmpI>=0:
                if A[tmpI][config[j]] == 1:
                    area = (i-tmpI+1)*(len(A[0])-j)
                    maxArea = max(maxArea,area)
                    tmpI-=1
                    continue    #possible it has more consicutive 1's i.e i=1 and j=2(actual index =0)
                j+=1
        return maxArea
                    