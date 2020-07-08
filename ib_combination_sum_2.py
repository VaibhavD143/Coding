class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        
        def rec(ind,sm):
            if sm == 0:
                res.append([A[i] for i in lst])
                # print(ind,res)
                return
            if sm<0 or ind>=len(A):
                return
            # print(ind,A[ind],A[ind-1])
            if A[ind-1] != A[ind] or (lst and lst[-1] == ind-1):
                lst.append(ind)
                rec(ind+1,sm-A[ind])
                lst.pop()
            rec(ind+1,sm)
        
        res = []
        lst = []
        A.sort()
        A = [-1]+A
        rec(1,B)
        return res

#         A = candidates
#         k = target
        
# #         if k == 0:
# #             return [[]]
# #         if not len(lst):
# #             return []
# #         res = [set() for i in range(k+1)]
# #         t_res = [set() for i in range(k+1)]
# #         lst.sort()
# #         for i in lst:
# #             for j in range(k+1):
# #                 for x in res[j]:
# #                     if i+j > k:
# #                         break
# #                     # res[i+j].add(x+(i,))
# #                     t_res[i+j].add(x+(i,))
# #             if i<=k:
# #                 t_res[i].add((i,))

# #             for j in range(k+1):
# #                 if t_res[j]:
# #                     res[j]=res[j].union(t_res[j])

# #         return res[-1]
        