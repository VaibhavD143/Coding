for tc in range(int(input())):
    n = map(int,input().split())
    lst = list(map(int,input().split()))
    dp = [0]*len(lst)
    res = 0
    cnt = 0
    for i in range(1,len(lst)):
        if lst[i]>lst[i-1]:
            dp[i]=1+dp[i-1]
        elif lst[i] == lst[i-1]:
            dp[i] = dp[i-1]
        if dp[i] == 4:
            res+=1
            dp[i] = 0
    for j in range(len(lst)-2,-1,-1):
        if lst[j] >lst[j+1]:
            dp[j] = dp[j+1]+1
        elif lst[j] == lst[j+1]:
            dp[j]=dp[j+1]

        if dp[j] == 4:
            res+=1
            dp[j] = 0

    print("Case #{}: {}".format(tc+1,res))