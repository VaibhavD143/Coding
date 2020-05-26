class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        A = [list(row) for row in A]
        # for row in A:
        #     print(row)
        ss = []
        cnt = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 'X':
                    cnt+=1
                    # print(i,j,cnt)
                    ss.append([i,j])
                    while ss:
                        node = ss.pop()
                        if 0<node[0] and A[node[0]-1][node[1]]=='X':
                            A[node[0]-1][node[1]] = cnt
                            ss.append([node[0]-1,node[1]])
                            
                        if node[0]<len(A)-1 and A[node[0]+1][node[1]]=='X':
                            A[node[0]+1][node[1]] = cnt
                            ss.append([node[0]+1,node[1]])
                            
                        if 0<node[1] and A[node[0]][node[1]-1] == 'X':
                            A[node[0]][node[1]-1]=cnt
                            ss.append([node[0],node[1]-1])
                            
                        if node[1]<len(A[0])-1 and A[node[0]][node[1]+1] == 'X':
                            A[node[0]][node[1]+1] = cnt
                            ss.append([node[0],node[1]+1])
        return cnt