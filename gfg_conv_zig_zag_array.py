for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    max_elem = lst[-1]+1
    left = 0
    right = n-1
    for i in range(n):
        if not i&1:
            lst[i] += lst[right]%max_elem * max_elem
            right -=1
        else:
            lst[i] += lst[left]%max_elem * max_elem
            left +=1
    
    for i in range(n):
        lst[i] = lst[i]//max_elem
    
    print(*lst)