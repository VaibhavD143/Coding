"""
https://leetcode.com/problems/3sum/
triplates with sum 0
without repeatation of number
"""

lst = [-1, 0, 1, 2, -4]
l_lst = len(lst)
dic = {}

for i in lst:
    dic[i] = 0
res = set()
for i in range(l_lst):
    dic[lst[i]]=i+1
    for j in range(i+1,l_lst):
        if dic[lst[j]] <= i:
            dic[lst[j]]=i+1
            try:
                if dic[-lst[i]-lst[j]]<=i:
                    res.add((lst[i],lst[j],-lst[i]-lst[j]))
                    dic[-lst[i]-lst[j]] = i+1
                else:
                    dic[lst[j]] = i
            except:
                pass
    del dic[lst[i]]
print(res)