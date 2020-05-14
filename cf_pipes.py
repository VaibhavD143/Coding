"""
https://codeforces.com/problemset/problem/1234/C
"""

for _ in range(int(input())):
    n = int(input())
    r=[[],[]]
    r[0] = input()
    r[1] = input()
    stck = [[1,n-1,-1]]
    flag = True
    while stck:
        x,y,direc=stck.pop()
        if x < 0 or y < 0:
            break

        if direc == -1:
            if r[x][y] == '1' or r[x][y] == '2':
                stck.append([x,y-1,-1])
                continue
            else:
                stck.append([1-x,y,1])
                continue
        else:
            if r[x][y] == '1' or r[x][y] == '2':
                flag = False
                break
            else:
                stck.append([x,y-1,-1])
                continue
    
    if flag and x==0 and y == -1:
        print("YES")
    else:
        print("NO")