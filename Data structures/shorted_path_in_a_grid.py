"""
Hadlock's detour algo : 
It is algo to find distance between two cells in a GRID
Intution : we do dfs travers on manhatten distance, because that is the shortest possible distance between two cell in a grid
- if we move any step further other than path then we will have to recover by moving back that distance, that's why `detour*2`
- so initially we try with detour=0, if path found then return, o/w we try path with detour = 1 which contribute 1*2=2 in result as we will have to recover that one distance.
Ref : https://leetcode.com/problems/cut-off-trees-for-golf-event/discuss/107396/Python-solution-based-on-wufangjie's-(Hadlock's-algorithm)
"""
def hadlock(matrix,x1,y1,x2,y2):
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
                    if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) and matrix[nx][ny]:
                        if closure:
                            current.append((nx,ny))
                        else:
                            nxt.append((nx,ny))
    return float('inf')