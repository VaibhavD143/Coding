class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        num = A[0]
        cnt=1
        for i in A[1:]:
            if i == num:
                cnt+=1
            else:
                cnt-=1
                if cnt<0:
                    cnt=1
                    num = i
        return num        