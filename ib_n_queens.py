"""
gyaan:
Better faster solution is possible
"""
class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        def isValid(pos,queens):
            # print(pos,queens)
            for (x,y) in queens:
                if pos[0] == x or pos[1]==y:
                    return False
                if abs(pos[0]-x) == abs(pos[1]-y):
                    return False
            return True
        
        def run(n,board,queens,res):
            if n ==-1:
                res.append([''.join(r) for r in board])
            for i in range(len(board)):
                if isValid((n,i),queens):
                    board[n][i]='Q'
                    run(n-1,board,queens+[[n,i]],res)
                    board[n][i]='.'
        board = [['.']*A for _ in range(A)]
        res =[]
        run(A-1,board,[],res)
        return res
#LEETCODE

# def solveNQueens(self, n):
#     def DFS(queens, xy_dif, xy_sum):
#         p = len(queens)
#         if p==n:
#             result.append(queens)
#             return None
#         for q in range(n):
#             if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
#                 DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
#     result = []
#     DFS([],[],[])
#     return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]