from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):
        parent = [-1]*A
        digit = [False]*A
        rem = 1%A
        parent[rem]=None
        digit[rem]=True
        ss = deque([rem])
        while ss:
            node= ss.popleft()
            
            mod0 = (node*10)%A
            mod1 = (node*10+1)%A
            if parent[mod0]==-1:
                parent[mod0] = node
                digit[mod0] = False
                ss.append(mod0)
            if parent[mod1] == -1:
                parent[mod1] = node
                digit[mod1] = True
                ss.append(mod1)
                
            if mod0 ==0 or mod1 ==0:
                break
            
        i=0
        res=""
        while i !=None:
            res+="1" if digit[i] else "0"
            i=parent[i]
        return res[::-1]