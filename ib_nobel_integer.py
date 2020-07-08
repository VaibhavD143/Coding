class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)
        for i,val in enumerate(A):
            if i ==0  or A[i]!=A[i-1]:  #to avoid repeating numbers
                if i==val:
                    return 1
        return -1