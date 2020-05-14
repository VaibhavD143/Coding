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
    return mid-1 #to return index of one lesser present number
	# return -1 #to return -1 if not present


lst1 = [1,2,4]
lst2 = [3,5]

if len(lst1) > len(lst2):
    lst1,lst2 = lst2,lst1

cnt = (len(lst1)+len(lst2))//2

