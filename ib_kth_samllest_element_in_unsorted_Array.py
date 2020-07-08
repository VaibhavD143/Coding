class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        def countSmaller(target):
            cnt=0
            for i in A:
                if i<=target:
                    cnt+=1
            return cnt
        low = min(A)
        high = max(A)
        while low<high:
            mid = low+(high-low)//2
            cnt = countSmaller(mid)
            # print(low,mid,high,cnt)
            if cnt<B:
                low=mid+1
            else:
                high=mid
        return low