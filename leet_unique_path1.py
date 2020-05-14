"""
https://leetcode.com/problems/unique-paths/
"""
n1= min(m,n)-1
n2 = max(m,n)-1
ans = div = 1
for i in range(n2+1,n2+n1+1):
    ans*=i
for i in range(1,n1+1):
    div*=i
print(ans//div)
    