class Solution:
    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        
        def isValid(n,i,j):
            if n in rows[i] or n in cols[j] or n in box[(i//3)*3+(j//3)]:
                return False
            return True

        def helper(ind):
            if ind == len(blanks):
                return True
            
            x,y = blanks[ind]
            for i in range(1,10):
                if isValid(i,x,y):
                    rows[x].append(i)
                    cols[y].append(i)
                    box[(x//3)*3+(y//3)].append(i)
                    # res[ind] = i
                    A[x][y]=str(i)
                    if helper(ind+1):
                        return True
                    rows[x].pop()
                    cols[y].pop()
                    box[(x//3)*3+(y//3)].pop()
            return False
        
        blanks = []
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        box = [[] for _ in range(9)]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] =='.':
                    blanks.append((i,j))
                else:
                    rows[i].append(int(A[i][j]))
                    cols[j].append(int(A[i][j]))
                    box[(i//3)*3+(j//3)].append(int(A[i][j]))
        # res = [None]*len(blanks)
        helper(0)