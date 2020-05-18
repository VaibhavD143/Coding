# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # @param A : root node of tree
    # @return an integer
    res=0
    def sumNumbers(self, A):
        
        def calc(root,num):
            if not root:
                return
            num*=10
            num+=root.val
            if not root.left and not root.right:
                self.res+=num
            calc(root.left,num)
            calc(root.right,num)
        self.res=0
        calc(A,0)
        return self.res