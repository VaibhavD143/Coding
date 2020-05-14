# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        q = deque([root])
        lev = 0
        res = []
        while q:
            q.append(-1)
            t_res = []
            while 1:
                elem = q.popleft()
                if elem == -1:
                    break
                if elem.left:
                    q.append(elem.left)
                if elem.right:
                    q.append(elem.right)
                t_res.append(elem.val)
            if lev:
                res.append(reversed(t_res))
                lev = 0
            else:
                res.append(t_res)
                lev =1
            
        return res