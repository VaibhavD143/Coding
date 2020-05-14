class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if not A or not A[0]:
            return 0
        lcol = [r[-1] for r in A]
        def binary_search(lst,target):
            #will return index of element if present of next greater element
            #in case grater than list then last element
            l=0
            r=len(lst)-1
            if l==r:
                if lst[0] == target:
                    return 0
            while l<r:
                mid = (l+r)//2
                
                if lst[mid] == target:
                    return mid
                
                elif lst[mid]<target:
                    l=mid+1
                else:
                    r=mid
            return r #return l
        rind = binary_search(lcol,B)
        # print(rind)
        ind = binary_search(A[rind],B)
        return 0 if A[rind][ind] != B else 1