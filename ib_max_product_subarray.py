class Solution:
    def maxProduct1(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        
        arr = nums
        t_min = arr[0]
        t_max = arr[0]
        g_max = arr[0]

        for i in range(1,len(arr)):
            if arr[i]<0:
                t_min,t_max = t_max,t_min

            t_min = min(arr[i],t_min*arr[i])
            t_max = max(arr[i],t_max*arr[i])

            g_max = max(t_max,g_max)
        return g_max
    def maxProduct(self, A: List[int]) -> int:
        B = A[::-1]
        
        for i in range(1, len(A)):
            A[i] = A[i]*(A[i-1] or 1)
            B[i] = B[i]*(B[i-1] or 1)
        # print(A,B)
        return max(A+B)

    def maxProduct2(self, A):
        if len(A)==1:
            return A[0]
        res = max(A)
        minn = 1
        maxn = 1
        flag = 0
        for i in range(len(A)):
            if A[i]>0:
                maxn*=A[i]
                minn= min(minn*A[i],1)
                flag = 1
            elif A[i]<0:
                newmin = maxn*A[i]
                newmax = max(minn*A[i],1)
                minn = newmin
                maxn = newmax
            else:
                # res = max(res,maxn)
                maxn=1
                minn=1
                # continue
            res = max(res,maxn)
            # print(res,i)
        if flag == 0 and res == 1:
            return 0
        return res