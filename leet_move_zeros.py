"""
https://leetcode.com/problems/move-zeroes/
"""

lst = [0,1,0,3,12]
ind = 0
for i in range(len(lst)):
    if lst[i]!=0:
        lst[i],lst[ind] = lst[ind],lst[i]
        ind+=1
print(lst)