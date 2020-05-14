def mod_a(inp):
    return [int(inp),'a']
def mod_d(inp):
    return [int(inp),'d']
for _ in range(int(input())):
    n = int(input())
    arr = list(map(mod_a,input().split()))
    dep = list(map(mod_d,input().split()))

    eves = sorted(arr+dep)
    
    min_p = 0
    cnt=0
    for eve in eves:
        if eve[1] == 'a':
            cnt +=1
        else:
            cnt-=1
        if min_p < cnt:
            min_p = cnt
    print(min_p)