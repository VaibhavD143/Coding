# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def rec(root):
            if not root:
                return [0,0]
            nonlocal res
            left = rec(root.left)
            right = rec(root.right)
            res = max(res,1+left[1],1+right[0])
            return [1+left[1],1+right[0]]
        res = 1
        rec(root)
        
        return res-1