import math
tc = int(input())
while tc:
    n,k = map(int,input().strip().split())
    s = input()
    prev = -1
    res = 0
    for i,ch in enumerate(s):
        if ch == '1':
            if prev ==-1:
                space = i
                block = space
            else:
                space = i-prev-1
                block = space-k
            res+=(block//(k+1))
            # print(prev,i,block)
            prev=i
    space = len(s)-prev-1
    if prev == -1:
        res+= math.ceil(space/(k+1))
        # print(space,k+1)
    else:
        res+=space//(k+1)
    print(res)
    tc-=1