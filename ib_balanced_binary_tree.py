# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        def isValid(root):
            if not root:
                return 0
            
            l = isValid(root.left)
            if l ==-1:
                return -1
            r = isValid(root.right)
            if r == -1:
                # print(root.val)
                return -1
            return 1+max(l,r) if -1<=l-r<=1 else -1
        l = isValid(A.left)
        if l == -1:
            return 0
        r = isValid(A.right)
        if r == -1:
            return 0
        return 1 if -1<=l-r<=1 else 0