for tc in range(int(input())):
    res=0
    input()
    lst = list(map(int,input().split()))
    for i in range(1,len(lst)-1):
        res+=(lst[i-1]<lst[i] and lst[i]>lst[i+1])
    print('Case #{}: {}'.format(tc+1,res))