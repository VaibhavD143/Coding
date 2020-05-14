"""
https://www.geeksforgeeks.org/longest-subarray-with-first-element-greater-than-or-equal-to-last-element/
Given an array consisting of integers, design an efficient algorithm to compute
the length of the longest sub array, where the first element in the sub array is
>= last element in the sub array.
"""
def binary_search(lst,elm):
	f = 0
	r = len(lst)
	pmid = -1
	mid = (f+r) //2

	while f != r:

		# print('in',f,mid,r)
		if lst[mid][0] == elm:
			return mid
		elif lst[mid][0] > elm:
			r = mid
		else:
			f = mid+1
		
		pmid = mid
		mid = (f+r) //2
	
	return lst[mid][1] #to return index of next present number
	
lst = [-5, -1, -55, 7, 1, -2]
# lst = [1,5,7]
l_lst = len(lst)
search_space =[[lst[0],0]]

for i in range(1,l_lst):
    if lst[i] > search_space[-1][0]:
        search_space.append([lst[i],i])
maxLen = 0
print(lst,search_space)
for i in range(l_lst):
    ind = binary_search(search_space,lst[i])
    if maxLen < (i-ind):
        maxLen = i-ind
        sind = ind
        eind = i
print(maxLen+1)