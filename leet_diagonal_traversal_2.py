"""
1)
>convert each row into deque, so we can perform popleft operation faster
>rows : contains index of rows having elements yet to be processed
>for each row, iterate in reverse order from rows till first row and pop left element in result
>if list becomes empty then remove it from rows list
>repeat it till rows becomes empty
2)
>Intution :
    -all the cell having equal sum(i+j) will be in a same diagonal.(i = row index, j = column index)
    -in result higher row index i comes first on equal sum(i+j). i.e nums[1][0] comes before nums[0][1]
>create a dictionary(HashTable) ha and append elements into keys as sum of row and column index
>Iterate keys in increasing order and append reversed list to result as per the 2nd condition established in intution
"""
from collections import defaultdict
def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#         res = []
#         rows=[0]
#         nums = deque([deque(r) for r in nums])
#         cnt=0
#         cnt+=1
#         while rows:
#             for i in rows[::-1]:
                
#                 res.append(nums[i].popleft())
#                 if not nums[i]:
#                     rows.remove(i)
#             if cnt<len(nums):
#                 rows.append(cnt)
#                 cnt+=1
#         return res

        ha = defaultdict(list)
        for i,row in enumerate(nums):
            for j,val in enumerate(row):
                ha[i+j].append(val)
        res = []
        for key in sorted(ha.keys()):
            res.extend(reversed(ha[key]))
        
        return res
                