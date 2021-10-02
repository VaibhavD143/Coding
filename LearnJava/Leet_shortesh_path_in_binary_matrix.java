import java.util.*;
class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        
        if (grid.length == 0 || grid[0].length == 0 || grid[0][0] == 1 || grid[grid.length-1][grid[0].length-1] == 1) {
            return -1;
        }
        
        int[][] mat = new int[grid.length][grid[0].length];
        for (int i=0; i<grid.length; i++) {
            Arrays.fill(mat[i], 0);
        }
        
        int[][] dirs = {
            {1,0},{1,1},{1,-1},{0,1},{0,-1},{-1,0},{-1,1},{-1,-1},
        };
        
        Deque<int[]> stack = new LinkedList<>();
        
        stack.offer(new int[]{0,0,1});
        mat[0][0] = 1;
        
        while (!stack.isEmpty()) {
            int[] elem = stack.poll();
            
            for (int[] dir : dirs) {
                int x = elem[0] + dir[0];
                int y = elem[1] + dir[1];
                
                if (x == grid.length && y == grid[0].length) {
                    return elem[2];
                }
                
                if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length && grid[x][y] == 0 && mat[x][y] == 0) {
                    stack.add(new int[]{x, y, elem[2] + 1});
                    mat[x][y] = 1;
                }
            }
        }
        
        return -1;
    }
}