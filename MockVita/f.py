def run():
    board= [[0]*12 for _ in range(12)]
    ang = input()
    ax,ay = int(ang[1:])-1,ord(ang[0])-ord('A')

    st = input().split('|')
    cords = input().split("|")
    for name,c in zip(st,cords):
        if name == 'E':
            ex,ey = int(c[1:])-1,ord(c[0])-ord('A')
        if name == 'M':
            mx,my = int(c[1:])-1,ord(c[0])-ord('A')
        if name == 'L':
            lx,ly = int(c[1:])-1,ord(c[0])-ord('A')
    # print(ax,ay)
    # print("m",mx,my)
    # print("e",ex,ey)
    # print("l",lx,ly)
    c = 1
    for i in range(12):
        if ax == 0:
            board[ax+i][ay] = c
        elif  ax==11:
            board[ax-i][ay] = c
        elif ay==0:
            board[ax][ay+i] = c
        else:
            board[ax][ay-i] = c
        c+=1
    # print(0,list(range(12)))
    # for i,r in enumerate(board):
    #     print(i,r)
    mx1,mx2 = min(mx,11-mx),max(mx,11-mx)
    my1,my2 = min(my,11-my),max(my,11-my)
    
    res = ""
    resx = None
    resy = None
    #muto
    if board[mx1][my1] != 0:
        resx = mx1
        resy = my1
        res = "MOTU"     
    if board[mx1][my2]!=0:
        resx = mx1
        resy = my2
        res = "MOTU"
    if board[mx2][my1] !=0:
        resx = mx2
        resy = my1
        res = "MOTU"
    if board[mx2][my2] != 0:
        resx = mx2
        resy = my2
        res = "MOTU"
    # print(res,resx,resy)
    #eek
    d=1
    for i in range(12):
        # print(ex,ey)
        if board[ex][ey] == i+1:
            if res!= "":
                if board[resx][resy] > board[ex][ey]:
                    resx = ex
                    resy = ey
                    res = "eek"
                elif board[resx][resy] == board[ex][ey]:
                    res = "dies"
                break
            else:
                resx,resy = ex,ey
                res = "eek"
            break
        if ex-1 !=-1 and ey+1!= 12 and board[ex-1][ey+1] == i+1:
            if res!= "":
                if board[resx][resy] > board[ex-1][ey+1]:
                    resx = ex-1
                    resy = ey+1
                    res = "eek"
                elif board[resx][resy] == board[ex-1][ey+1]:
                    res = "dies"
                break
            else:
                resx,resy = ex-1,ey+1
                res = "eek"
            break
        if ex != 11 and ey!= 0  and board[ex+1][ey-1]==i+1:
            if res!= "":
                if board[resx][resy] > board[ex+1][ey-1]:
                    resx = ex+1
                    resy = ey-1
                    res = "eek"
                elif board[resx][resy] == board[ex+1][ey-1]:
                    res = "dies"
                break
            else:
                resx,resy = ex+1,ey-1
                res = "eek"
            break
        if ex-1==0 or ex+1 == 11 or ey-1 == 0 or ey+1 ==11:
            d=-1*d
        ex-=d
        ey-=d
        
    # print(res,resx,resy)
    #lego
    dx=dy=0
    
    if lx == 0:
        dx=1
        steps = max(ly,11-ly)
    elif lx == 11:
        dx=-1
        steps = max(ly,11-ly)
    if ly == 0:
        dy = 1
        steps = max(lx,11-lx)
    elif ly == 11:
        dy=-1
        steps = max(lx,11-lx)
    s = steps
    time = 15
    for i in range(12):
        # print(i+1,lx,ly)
        if board[lx][ly] >i:
            if board[lx][ly]<time:
                time = board[lx][ly]
                if res=="" or board[resx][resy]<board[lx][ly]:
                    res ="dies"
                    resx = lx
                    resy = ly
        s-=1
        if s == -1:
            s = steps-1
            if dy !=0:
                dy =0 
            else:
                if ly>11-ly:
                    dy=-1
                else:
                    dy=1
            if dx != 0:
                dx = 0
            else:
                if lx>11-lx:
                    dx=-1
                else:
                    dx=1
        lx+=dx
        ly+=dy
    return res,resx,resy
res,x,y = run()
if res == "":
    print("WON")
elif res == "MOTU":
    print("MUTO")
else:
    dim = chr(ord('A')+y)+str(x+1) 
    print(dim)