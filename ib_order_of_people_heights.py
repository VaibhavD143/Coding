"""
Swapping is costlier than insert function!
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        if not A :
            return A
        lst = list(zip(A,B))
        # print(lst)
        lst.sort()
        res = []
        # print(lst)
        # for i in range(len(A)-1,-1,-1):
            # for j in range(i,i+lst[i][1]):
            #     lst[j],lst[j+1]=lst[j+1],lst[j]
        for val,i in lst[::-1]:
            res.insert(i,val)
        return res
        