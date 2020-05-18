class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        if not A:
            return []
        def run(A,start,ind,lst,res):
            # print(start,ind,lst,res)
            if ind==len(A):
                if start == ind:
                    res.append(lst)
                return
            
            if A[start:ind+1]==A[start:ind+1][::-1]:
                
                added = lst+[A[start:ind+1]]
                run(A,ind+1,ind+1,added,res)
            run(A,start,ind+1,lst,res)
        res=[]
        run(A,0,0,[],res)
        # print(len(res))
        return res
# def partition(self, s):
#     res = []
#     self.dfs(s, [], res)
#     return res

# def dfs(self, s, path, res):
#     if not s:
#         res.append(path)
#         return
#     for i in range(1, len(s)+1):
#         if self.isPal(s[:i]):
#             self.dfs(s[i:], path+[s[:i]], res)
    
# def isPal(self, s):
#     return s == s[::-1]
            