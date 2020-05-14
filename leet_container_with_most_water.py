"""
https://leetcode.com/problems/container-with-most-water/
"""

lst = [7,2,3,12,7]
l,r=0,len(lst)-1
c_max = 0
while l<r:
    if lst[l]<lst[r]:
        c_max = max(c_max,lst[l]*(r-l))
        l+=1
    else:
        c_max = max(c_max,lst[r]*(r-l))
        r-=1
print(c_max)