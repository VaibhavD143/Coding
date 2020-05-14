"""
https://leetcode.com/problems/top-k-frequent-elements/
"""
import collections

lst = [4,1,1,1,2,2,3]
dic = {}
k=3
for i in lst:
    dic[i]=dic.get(i,0)+1
s_lst = sorted(dic.items(),key=lambda kv:kv[1],reverse=True)
print([x[0] for x in s_lst[:k]])