"""
find max sum of subarray with length exactly L
"""

lst = [2,4,-3,8,9]
l_lst = len(lst)
L=3

maxSum = sum(lst[:L])
tsum = maxSum

for i in range(L,l_lst):
    tsum = tsum-lst[i-L]+lst[i]
    if tsum>maxSum:
        maxSum = tsum

print(maxSum)