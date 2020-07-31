d = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
MOD = 10**9

def rec(lst,ind):
    # print(ind)
    i=ind+2
    difx,dify = 0,0
    x,y = 0,0
    while lst[i]!=')':
        if lst[i].isdigit():
            dx,dy,diff = rec(lst,i)
            i=diff
        else:
            dx,dy = d[lst[i]] 
            i+=1
        difx+=dx
        dify+=dy
    n = int(lst[ind])
    while n:
        x+=difx
        y+=dify
        n-=1
    # print(x,y,i+1)
    x%=MOD
    y%=MOD
    return x,y,i+1

for tc in range(int(input())):
    lst = '1('+input()+')'
    x,y,_ = rec(lst,0)
    x = 1 if x == MOD else x+1
    y = 1 if y == MOD else y+1

    print(F"Case #{tc+1}: {y} {x}")