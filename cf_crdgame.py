for _ in range(int(input())):
    n = int(input())
    c1 = c2 = 0
    for _ in range(n):
        x,y = input().split()
        s1=s2=0
        for c in x:
            s1+=int(c)
        for c in y:
            s2+=int(c)

        if s1 <= s2:
            c2+=1
        if s1>=s2:
            c1+=1
    if c1 == c2:
        print(F'2 {c1}')
    elif c1>c2:
        print(F'0 {c1}')
    else:
        print(F'1 {c2}')