"""
https://leetcode.com/problems/first-missing-positive/
"""

lst = [1,1,1,2]
i=0
while i <len(lst):
    if lst[i]>0 and lst[i]<=len(lst):
        ind = lst[i]-1
        if lst[ind]!=lst[i]:
            lst[ind],lst[i] = lst[i],lst[ind]
            i-=1
    i+=1
print(lst)
flag =1
for i in range(len(lst)):
    if i+1 != lst[i]:
        print(i+1)
        flag = 1
        break
if not flag:
    print(len(lst)+1)