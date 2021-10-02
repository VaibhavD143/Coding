class Solution {
    public boolean dfs(char[][] board,String word,int i,int j,int ind,boolean[][] vis){
        if(ind == word.length()){
            return true;
        }
        for(int[] dir:new int[][]{{1,0},{0,1},{-1,0},{0,-1}}){
            int ni = i+dir[0];
            int nj = j+dir[1];
            if(ni>=0 && ni<board.length && nj>=0 && nj<board[0].length && vis[ni][nj] == false && board[ni][nj]==word.charAt(ind)){
                vis[ni][nj] = true;
                if(dfs(board,word,ni,nj,ind+1,vis)) return true;
                vis[ni][nj] = false;
            }
        }
        return false;
    }
    
    public boolean exist(char[][] board, String word) {
        boolean[][] vis = new boolean[board.length][board[0].length];
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                if(board[i][j]==word.charAt(0)){
                    vis[i][j] = true;
                    if(dfs(board,word,i,j,1,vis)) return true;
                    vis[i][j] = false;
                }
            }
        }
        return false;
    }
    
}