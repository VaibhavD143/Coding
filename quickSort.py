import time
import math
def quickSort(a,left,right):
	if(right-left <= 1):
		return()
	first=left+1
	for second in range(left+1,right):
		if(a[second] < a[left]):
			(a[first],a[second])=(a[second],a[first])
			first+=1
	(a[first-1],a[left])=(a[left],a[first-1])
	quickSort(a,left,first-1)
	quickSort(a,first,right)
# quickSort(a,0,len(a))
# print(a)

