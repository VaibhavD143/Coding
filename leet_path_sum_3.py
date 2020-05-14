from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

# 0
lst = [10,5,-3,3,2,None,11,3,-2,None,1]
root = deserialize('[5,null,1,-1,null,1,null,-1]')
target = 5
root = deserialize('[10,5,-3,3,2,null,11,3,-2,null,1]')
target = 8
root = deserialize('[1,-1,null,1,null,-1]]')
target = 0
ss = deque([[root,[target]]])
cnt=0
while ss:
    node,sumLst = ss.popleft()
    nxtLst = [target]
    for i in sumLst:
        rem = i-node.val
        if rem == 0:
            cnt+=1
        nxtLst.append(rem)
    if node.left:
        ss.append([node.left,nxtLst])
    if node.right:
        ss.append([node.right,nxtLst])
    print(node.val,ss,cnt)
print(cnt)