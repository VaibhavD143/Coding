"""
find max sum of subarray with length atmost L
"""

lst = [8,5,-10,5,6,2]
# lst = [2,6,-9,8,5,-10,5,6,2]
l_lst = len(lst)
L = 4

maxSum = lst[0]
tsum = maxSum
sq = [0]
sind = eind = 0
for i in range(1,l_lst):
	while sq and L<= i-sq[0]:
		ind = sq.pop(0)
		tsum = tsum-lst[ind]
	
	if lst[i] > tsum+lst[i]:
		sq = [i]
		tsum = lst[i]
	else:
		tsum+=lst[i]
		sq.append(i)
	
	if tsum > maxSum:
		maxSum = tsum
		sind = sq[0]
		eind = i
print(maxSum)
print(sind,eind)