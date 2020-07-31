def isDivisible(arr,m):
    if len(arr)>m:
        return True
    
    dp1 = [False]*(m+1)
    dp1[0] = True
    # dp2 = dp1[:]
    arr.sort(reverse =True)
    for n in arr:
        dp2=dp1[:]
        for i in range(len(dp1)):
            if dp1[i]:
                sm = i+n
                if sm%m==0:
                    print(sm,n)
                    return True
                dp2[sm%m] = True
        dp1=dp2
    return False


arr = [3, 1, 7, 5]
arr = [1,6]
m = 5
print(isDivisible(arr,m))