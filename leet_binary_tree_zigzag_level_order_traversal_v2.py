# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        res = [[root.val]]
        
        def trav(lst,flag):
            tres = []
            trow = []

            for i in reversed(lst):
                if i.right and flag:
                    tres.append(i.right.val)
                    trow.append(i.right)
                
                if i.left:
                    tres.append(i.left.val)
                    trow.append(i.left)
                
                if i.right and not flag:
                    tres.append(i.right.val)
                    trow.append(i.right)
            if tres:
                res.append(tres)
            return trow
        
        row= [root]
        flag = 1
        while row:
            print(res)
            row = trav(row,flag)
            flag = 1 -flag
        return res