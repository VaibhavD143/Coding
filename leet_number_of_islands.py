"""
https://leetcode.com/problems/number-of-islands/
"""
r,c = map(int,input().split())
mat = []
for i in range(r):
    mat.append(input())
vis = [[0]*c for _ in range(r)]
cnt=1
for i in range(r):
    for j in range(c):
        if vis[i][j] == 0 and mat[i][j] != '0':
            stack = [[i,j]]
            while stack:
                x,y = stack.pop()
                vis[x][y] = cnt
                if x-1 >=0 and mat[x-1][y] == '1' and not vis[x-1][y]:
                    stack.append([x-1,y])
                if x+1 < r and mat[x+1][y] == '1' and not vis[x+1][y]:
                    stack.append([x+1,y])
                if y-1 >= 0 and mat[x][y-1] == '1' and not vis[x][y-1]:
                    stack.append([x,y-1])
                if y+1 < c and mat[x][y+1] == '1' and not vis[x][y+1]:
                    stack.append([x,y+1])
            cnt+=1
# for i in mat:
#     print(i)
# for i in vis:
#     print(i)
print(cnt-1)
