class Solution:
    def solve(self, A) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not A or not A[0]:
            return A
#         ss = []
#         for i in [0,len(A)-1]:
#             for j in range(len(A[0])):
#                 if A[i][j] == 'O':
#                     ss.append([i,j])
#                     A[i][j]=1
#                     while ss:
#                         node = ss.pop()
#                         if 0<node[0] and A[node[0]-1][node[1]]=='O':
#                             A[node[0]-1][node[1]] = 1
#                             ss.append([node[0]-1,node[1]])
                            
#                         if node[0]<len(A)-1 and A[node[0]+1][node[1]]=='O':
#                             A[node[0]+1][node[1]] = 1
#                             ss.append([node[0]+1,node[1]])
                            
#                         if 0<node[1] and A[node[0]][node[1]-1] == 'O':
#                             A[node[0]][node[1]-1]=1
#                             ss.append([node[0],node[1]-1])
                            
#                         if node[1]<len(A[0])-1 and A[node[0]][node[1]+1] == 'O':
#                             A[node[0]][node[1]+1] = 1
#                             ss.append([node[0],node[1]+1])
        
#         for j in [0,len(A[0])-1]:
#             for i in range(len(A)):
#                 if A[i][j] == 'O':
#                     ss.append([i,j])
#                     A[i][j]=1
#                     while ss:
#                         node = ss.pop()
#                         if 0<node[0] and A[node[0]-1][node[1]]=='O':
#                             A[node[0]-1][node[1]] = 1
#                             ss.append([node[0]-1,node[1]])
                            
#                         if node[0]<len(A)-1 and A[node[0]+1][node[1]]=='O':
#                             A[node[0]+1][node[1]] = 1
#                             ss.append([node[0]+1,node[1]])
                            
#                         if 0<node[1] and A[node[0]][node[1]-1] == 'O':
#                             A[node[0]][node[1]-1]=1
#                             ss.append([node[0],node[1]-1])
                            
#                         if node[1]<len(A[0])-1 and A[node[0]][node[1]+1] == 'O':
#                             A[node[0]][node[1]+1] = 1
#                             ss.append([node[0],node[1]+1])
        
        I,J = len(A),len(A[0])
        unsur = [ij for k in range(max(I,J)) for ij in [(0,k),(I-1,k),(k,0),(k,J-1)]]
        while unsur:
            i, j = unsur.pop()
            if i<0 or i>=I or j<0 or j>=J:
                continue
            if A[i][j] == 'O':
                A[i][j] = 1
                unsur.append((i-1,j))
                unsur.append((i+1,j))
                unsur.append((i,j-1))
                unsur.append((i,j+1))
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    A[i][j]='O'
                else:
                    A[i][j]='X'
        return A
            