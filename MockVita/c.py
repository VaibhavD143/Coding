min_l = int(input())
max_l = int(input())
min_w = int(input())
max_w = int(input())
dp = {}
def rec(l,w):
    # print(l,w)
    if l==0 or w==0:
        return 0

    if (l,w) in dp:
        return dp[l,w]
    res = 1+rec(min(l,w-l),max(l,w-l))
    dp[l,w] = res
    return res
res = 0
for i in range(min_l,1+max_l):
    for j in range(min_w,1+max_w):
        res+=rec(min(i,j),max(i,j))
        # print(i,j,res)
print(res)