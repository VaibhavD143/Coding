import time
import math

def find_index(a,l):
	ind = 0
	val = a[0]
	for i in range(1,l):
		if val> a[i]:
			ind = i
			val = a[i]
	return ind

def randmisedQS(a,left,right):
	# left to right where left inclusive and right exclusive
	if right-left < 2:
		return None

	ind = find_index(a[left:right],int(math.log(right-left,2)))+left
	a[left],a[ind] = a[ind],a[left]
	# print(a[left])
	first = left
	for second in range(left+1,right):
		if a[left] >= a[second]:
			first+=1
			a[first],a[second] = a[second],a[first]
	a[left],a[first] = a[first],a[left]
	randmisedQS(a,left,first)
	randmisedQS(a,first+1,right)

a=list(range(int(1e2)))
start = time.time()
randmisedQS(a,0,int(1e2))
print(time.time() - start)
print(a)