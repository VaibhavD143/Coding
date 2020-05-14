"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""
lst = [4]
dp = {}
for i in lst:
    if dp.get(i,None) == None:
        dp[i] = 1
    else:
        del dp[i]
print(list(dp.keys())[0])
res = 0
for i in lst:
    res ^= i
print(res)

print(2*sum(set(lst))-sum(set(lst)))