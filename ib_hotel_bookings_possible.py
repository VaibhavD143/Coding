class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arr, dep, n):
        if n == 0:
            if arr:
                return 0
            else:
                return 1
        lst = []
        arr.sort(reverse=1)
        dep.sort(reverse=1)
        flag =1
        res=0
        # while arr:
        #     if flag:
        #         if arr[-1]<=dep[-1]:
        #             arr.pop()
        #             res+=1
        #             flag=0
        #         else:
        #             dep.pop()
        #             res-=1
        #             flag=1
        #     else:
        #         if dep[-1]<=arr[-1]:
        #             dep.pop()
        #             res-=1
        #             flag=1
        #         else:
        #             arr.pop()
        #             res+=1
        #             flag=0
        #     if res>n:
        #         return False
        # return True
        while arr and dep:
            k = min(arr[-1],dep[-1])
            if dep[-1] == k:
                res-=1
                dep.pop()
            else:
                res+=1
                arr.pop()
            if res>n:
                return False
        if arr and res+1>n:
            return False
        return True
                
