"""
https://leetcode.com/problems/diagonal-traverse
"""

dir = {0:[1,0],1:[0,1]}
dir_cord = {0:[1,-1],1:[-1,1]}
mat = [
    [ 1, 2, 3,10,11 ],
    [ 4, 5, 6,12,13 ],
    [ 7, 8, 9,14,15 ]]
mat=[
    [1,2,3,4],
    [5,6,7,8]
    ]
r= len(mat)
c=len(mat[0])
tot=0
d = 1
x=y=0
while tot<=(r+c-2):
    print(x,y,'start')
    while x<r and y<c and x>=0 and y>=0:
        print(mat[x][y])
        x+=dir_cord[d][0]
        y+=dir_cord[d][1]
    x-=dir_cord[d][0]
    y-=dir_cord[d][1]
    print(x,y,'end',d)
    if x == r-1 and d == 0:
        y+=1
    elif d == 1 and y == c-1:
        x+=1
    else:
        x+=dir[d][0]
        y+=dir[d][1]
    d=1-d
    tot+=1
    print(tot,'total')
