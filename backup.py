"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
unsolved
"""
import math
def binary_search(lst,elm):
    f = 0
    r = len(lst)
    pmid = -1
    mid = (f+r) //2

    while f != r:
        if lst[mid] == elm:
            return mid
        elif lst[mid] > elm:
            r = mid
        else:
            f = mid+1

        pmid = mid
        mid = (f+r) //2
    return mid-1 #to return index of next present number
	# return -1 #to return -1 if not present


lst1 = [1,2,3]
lst2 = [4,5]

l_l1 = len(lst1)
l_l2 = len(lst2)

if l_l1>l_l2:
    l_l1,l_l2 = l_l2,l_l1
    lst1,lst2 = lst2,lst1
ind = math.ceil((l_l1+l_l2)/2)-1
disc = 0
ind1 = -1
ind2 = 0
while 1:
    loc_ind21 = binary_search(lst1,lst2[ind2])
    if loc_ind21+ind2+2 >=ind+1:
        break
    ind1 = loc_ind21
    ind2+=1
print(ind1,loc_ind21,ind2)
rem = ind+1-(ind1+1)-(ind2+1)
if ind1+1+rem >= len(lst1):
    print(lst2[ind-len(lst1)])
else:
    print(lst1[ind-ind2])
# if lst2[ind2]>=lst1[-1]:
#     #when list1 is completely ignored
#     a_ind = ind-ind2+1-len(lst1)
#     if a_ind ==0:
#         #when last element of first list is answer
#         print(lst1[-1],'1')
#     else:
#         #answer is from 2nd list
#         print(lst2[a_ind],'2')
# else:
#     if ind1 == -1:
#         #when only second list is givning answer
#         print(lst2[ind],'3')
#     else:
#         #when both takes part
#         if loc_ind21 == ind1:
#             #when contineous increament in 2nd so answer in list2
#             print(lst2[ind2],'4')
#         else:
#             #when including 2nd's element exceeds the required index so answer from lst1
#             print(lst1[ind-ind2],'5')