class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        left=[A[0]]
        right=[-1]*len(A)
        right[-1]=A[-1]
        for i in A[1:]:
            left.append(max(left[-1],i))
        for j in range(len(A)-2,-1,-1):
            right[j]=max(right[j+1],A[j])
        # print(A)
        # print(left)
        # print(right)
        water=0
        for i in range(len(A)):
            water+=max(0,min(left[i],right[i])-A[i])
        return water