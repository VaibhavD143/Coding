class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arr, dep, n):
        lst = []
        arr.sort(reverse=1)
        dep.sort(reverse=1)
        flag =1
        res=0
        while arr:
            if flag:
                if arr[-1]<=dep[-1]:
                    arr.pop()
                    res+=1
                    flag=0
                else:
                    dep.pop()
                    res-=1
                    flag=1
            else:
                if dep[-1]<=arr[-1]:
                    dep.pop()
                    res-=1
                    flag=1
                else:
                    arr.pop()
                    res+=1
                    flag=0
            if res>n:
                return False
        return True