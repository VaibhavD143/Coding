"""
Intution:
sort list and find distance between consecutive pairs as per the order
How to find distance:
1) BFS : brute force solution, very slow
2) hadlock's detour algo : It is algo to find distance between two cells in a GRID
Intution of algo: we do dfs travers on manhatten distance, because that is the shortest possible distance between two cell in a grid
- if we move any step further other than path then we will have to recover by moving back that distance, that's why `detour*2`
- so initially we try with detour=0, if path found then return, o/w we try path with detour = 1 which contribute 1*2=2 in result as we will have to recover that one distance.
Ref : https://leetcode.com/problems/cut-off-trees-for-golf-event/discuss/107396/Python-solution-based-on-wufangjie's-(Hadlock's-algorithm)

"""
from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        lst =[(0,0,0)]+[(forest[i][j],i,j) for i in range(len(forest)) for j in range(len(forest[0])) if  forest[i][j]>1]
        lst.sort()
        
        def findDistance(x1,y1,x2,y2):
            dirs = [(0,-1),(-1,0),(0,1),(1,0)]
            dist=float('inf')
            seen = [[False for _ in range(len(forest[0]))] for _ in range(len(forest))]
            ss = deque([(x1,y1,0)])
            seen[x1][y1] = True
            while ss:
                x,y,c = ss.popleft()
                if x == x2 and y == y2:
                    dist = min(dist,c)
                    continue
                for d in dirs:
                    nx = x+d[0]
                    ny = y+d[1]
                    # print(x,y,nx,ny)
                    if 0<=nx<len(forest) and 0<=ny<len(forest[0]) and not seen[nx][ny] and dist>c+1 and forest[nx][ny]!=0:
                        ss.append((nx,ny,c+1))
                        seen[nx][ny] = True
            return dist


        def hadlock(x1,y1,x2,y2):
            manhattan = abs(x1-x2)+abs(y1-y2)
            current,nxt = [],[(x1,y1)]
            detour = -1
            seen = set()

            while nxt:
                current,nxt = nxt,[]
                detour+=1
                while current:
                    x,y = current.pop()
                    if x == x2 and y==y2:
                        return manhattan+2*detour
                    if (x,y) not in seen:
                        seen.add((x,y))
                        for (nx,ny,closure) in [(x+1,y,x<x2),(x-1,y,x>x2),(x,y+1,y<y2),(x,y-1,y>y2)]:
                            if 0<=nx<len(forest) and 0<=ny<len(forest[0]) and forest[nx][ny]:
                                if closure:
                                    current.append((nx,ny))
                                else:
                                    nxt.append((nx,ny))
            return float('inf')
        res = 0
        for i in range(1,len(lst)):
            # res += findDistance(lst[i-1][1],lst[i-1][2],lst[i][1],lst[i][2])
            res += hadlock(lst[i-1][1],lst[i-1][2],lst[i][1],lst[i][2])
            # print(i,res)
            if res == float('inf'):
                return -1
        return res