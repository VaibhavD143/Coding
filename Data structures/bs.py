"""
If in every step, 
we are reducing size by -1 or +1 
    then allow condintion to be 'while l<=r' 
other wise 
    it should be 'while l<r'

mid=(l+r)//2 endup on l if r-l =1, consider this
"""
def binary_S(lst,target)
    start, end = 0, len(lst)-1

	while start <= end :
		mid = (start + end) // 2
		# we found a match
		if lst[mid] == target :
			return mid
		# go on right side
		elif lst[mid] < target :
			start = mid + 1
		# go on left side
		else :
			end = mid - 1;
	# element is not present in list
	return -1



def binary_search(lst,elm):
	f = 0
	r = len(lst)
	pmid = -1
	mid = (f+r) //2

	while f != r:

		print('in',f,mid,r)
		if lst[mid] == elm:
			return mid
		elif lst[mid] > elm:
			r = mid
		else:
			f = mid+1
		
		pmid = mid
		mid = (f+r) //2
	return mid #to return index of next present number
	# return -1 #to return -1 if not present
lst = [2,3,5]
key = 6
lst = [3,5,7,9,11]
key = 12
print(binary_search(lst,key))

