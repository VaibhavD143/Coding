# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        res = float('-inf')
        def maxSum(root):
            if not root:
                return float('-inf')
            nonlocal res
            l = maxSum(root.left)
            r = maxSum(root.right)
            res = max(res,l+root.val,root.val,root.val+r,l+root.val+r)
            return max(l+root.val,root.val,root.val+r)
        maxSum(A)
        return res