"""
Intution:
- generate all the possible sum in ha and find minimum from their
- Keeping extra set as first element in each key-pair, to avaoid usage of same element twice for same sum
ex 8 4 4 4 4 2 2 2 2
"""
from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        ha = defaultdict(list)
        
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if ha[A[i]+A[j]]:
                    #
                    if i in ha[A[i]+A[j]][0] or j in ha[A[i]+A[j]][0]:
                        continue
                else:
                    ha[A[i]+A[j]].append(set())
                ha[A[i]+A[j]][0].add(i)
                ha[A[i]+A[j]][0].add(j)
                ha[A[i]+A[j]].append([i,j])
        res = []
        for lst in ha.values():
            if len(lst)>=3:
                if not res:
                    res = lst[1:3]
                elif res>lst[1:3]:
                    res= lst[1:3]
        return res[0]+res[1] if res else res