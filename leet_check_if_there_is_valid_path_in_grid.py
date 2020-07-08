"""
Intution:
at any time cell can move to one direction. cx,cy is current grid cell
two loops because if grid[0][0] has path [3,4] then we can start from any one of them!
d : cell style with path it is offering
1 : left edge, 2: upper edge, 3:right edge, 4: lower edge
nex : to get next cell co-ordinates from currrent cell with direction according to current
seen : if cell is already exist
prev : entry edge in current cell
enter : gives entry edge from direction
dx,dy : destination

"""
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        #no outer path in grid
        if grid[0][0]==5:
            return False

        d = {1 : [1,3], 2:[2,4],3:[1,4],4:[3,4],5:[1,2],6:[2,3]}
        nex = {1:[0,-1],2:[-1,0],3:[0,1],4:[1,0]}
        seen = [[False]*len(grid[0]) for _ in range(len(grid))]
        enter = {1:3,3:1,2:4,4:2}
        
        dx,dy= len(grid)-1,len(grid[0])-1
        
        cx,cy=0,0
        path = d[grid[0][0]]
        prev = path[0]
        while True:
            path = d[grid[cx][cy]]
            # print(cx,cy,path)
            #when there is no incoming path from previous cell to current cell
            if prev not in path:
                break
            if cx == dx and cy == dy:
                return True
            #as prev is used as incoming, otherone will be used for out-going
            nexD = prev^path[0]^path[1]
            seen[cx][cy] = True
            cx += nex[nexD][0]
            cy += nex[nexD][1]
            #if cell is out of grid or already visited
            if cx<0 or cx>=len(grid) or cy<0 or cy>=len(grid[0]) or seen[cx][cy]:
                # print("break2")
                break
            
            
            prev = enter[nexD]
        
        cx,cy=0,0
        path = d[grid[0][0]]
        #only if (0,0) had two ways to go out
        if path[1] != 4 or path[0] != 3:
            return False
        prev = path[1]
        # seen = [[False]*len(grid[0]) for _ in range(len(grid))]   #not required, will be repetation
        while True:
            path = d[grid[cx][cy]]
            if prev not in path:
                break
            
            if cx == dx and cy == dy:
                return True
            
            nexD = prev^path[0]^path[1]
            seen[cx][cy] = True
            cx += nex[nexD][0]
            cy += nex[nexD][1]
            
            if cx<0 or cx>=len(grid) or cy<0 or cy>=len(grid[0]) or seen[cx][cy]:
                break

            prev = enter[nexD]
        return False