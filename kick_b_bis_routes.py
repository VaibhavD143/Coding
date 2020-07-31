for tc in range(int(input())):
    n,last = map(int,input().split())
    lst = list(map(int,input().split()))
    for n in lst[::-1]:
        last = min(last,(last//n)*n)
    
    print("Case #{}: {}".format(tc+1,last))