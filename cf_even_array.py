tc = int(input())
while tc:
    input()
    lst = map(int,input().strip().split())
    odd=even = 0
    for i,val in enumerate(lst):
        if i&1:
            if not val&1:
                odd+=1
        else:
            if val&1:
                even+=1
    print(odd if odd==even else -1)
    tc-=1