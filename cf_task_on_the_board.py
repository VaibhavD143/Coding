tc = int(input())
while tc:
    s = sorted(input())
    n = int(input())
    lst = []
    zeros = []
    lst = list(map(int,input().split()))

    for i in range(n):
        if lst[i] == 0:
            zeros.append(i)
    res = [None]*n
    si=len(s)-1
    while zeros:
        while s[si] != s[si-len(zeros)+1]:
            si-=1
        for ind in zeros:
            res[ind] = s[si]
            si-=1
        while si>=0 and s[si]==s[si+1]:
            si-=1
        tzeros = []
        for i in range(n):
            if lst[i]<=0:
                continue
            for ind in zeros:
                lst[i]-=abs(i-ind)
            if lst[i] == 0:
                tzeros.append(i)
        zeros = tzeros
    print(''.join(res))  
            

    tc-=1