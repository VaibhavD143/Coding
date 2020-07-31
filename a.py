for tc in range(int(input())):
    n = map(int,input().split())
    lst = list(map(int,input().split()))
    res = 0
    mx = -1
    for i in range(len(lst)-1):
        if lst[i]>mx and lst[i]>lst[i+1]:
            res+=1
        mx = max(mx,lst[i])
    if lst[-1]>mx:
        res+=1
    print("Case #{}: {}".format(tc+1,res))