"""
https://leetcode.com/problems/sort-colors/
"""

lst = [2,0,2,1,1,0]
ind = 0
i=0
col = 0
while col<3:
    i=ind
    while i<len(lst):
        if lst[i] == col:
            lst[ind],lst[i] = lst[i],lst[ind]
            ind+=1
        i+=1
    col+=1
    