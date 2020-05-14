"""
https://leetcode.com/problems/all-paths-from-source-to-target/
"""

def find_path(node,graph,path,res):

    if node == len(graph)-1:
        path.append(node)
        res.append(path.copy())
        path.pop()
        return
    
    path.append(node)
    for i in graph[node]:
        find_path(i,graph,path,res)
    path.pop()
    return
graph = [[1,2], [3], [3], []]
n = len(graph)
path=[]
res=[]
find_path(0,graph,path,res)
print(res)