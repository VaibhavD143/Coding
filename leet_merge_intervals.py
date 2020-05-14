"""
https://leetcode.com/problems/merge-intervals/
"""
lst = [[1,3],[2,6],[8,10],[15,18]]
lst = [[2,3],[4,5],[6,7],[8,9],[1,10]]
# lst = [[1,4],[4,6]]
lst.sort()

res = [lst[0]]
for i in range(1,len(lst)):
    if res[-1][1]>=lst[i][0]:
        res[-1][1] = max(res[-1][1],lst[i][1])
    else:
        res.append(lst[i])
print(res)