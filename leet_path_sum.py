# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def isSum(root,s):
            if not root:
                return False
            if not root.left and not root.right and s-root.val == 0:
                return True

            return self.hasPathSum(root.left,s-root.val) or self.hasPathSum(root.right,s-root.val)
            
        return isSum(root,sum)