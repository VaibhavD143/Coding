# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

"""
lst = [-2,-4,-7,-8,-9]
l_lst = len(lst)
L = 5

maxSum = lst[0]
tsum = maxSum
sq = [0]
for i in range(1,L):
	tsum = max(tsum+lst[i],lst[i])
	if tsum>maxSum:
		maxSum = tsum
print(maxSum)
"""

for _ in range(int(input())):
    n,s = map(int,input().split())
    arr = list(map(int,input().split()))
    l = 0
    r = 1
    total = arr[l]
    while r<n:
        if total == s:
            break
        elif total < s:
            total += arr[r]
            r+=1
        else:
            total -= arr[l]
            l+=1
    
    while total > s:
        total-=arr[l]
        l+=1

    if not total == s:
        print(-1)
    else:
        print(l+1,r)
