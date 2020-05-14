"""
https://leetcode.com/problems/group-anagrams/
"""

lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
ha = {}
res = []
for s in lst:
    sort_s = ''.join(sorted(s))
    if  ha.get(sort_s,-1) == -1:
        ha[sort_s] = len(res)
        res.append([s])
    else:
        res[ha[sort_s]].append(s)
print(res)