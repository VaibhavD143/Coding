# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        
        def rec(root):
            if not root:
                return [float('inf'),float('-inf'),0]
            nonlocal res
            
            left = rec(root.left)
            right = rec(root.right)
            if root.val>left[1] and root.val<right[0]:
                res = max(res,left[2]+right[2]+root.val)
                return [left[0] if left[0] != float('inf') else root.val,right[1] if right[1]!=float('-inf') else root.val,left[2]+right[2]+root.val]
            
            return [float('-inf'),float('inf'),0]
        res= 0 
        rec(root)
        return res