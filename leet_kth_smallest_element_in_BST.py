# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ans=None
        self.k=k
        def inorder(root):
            if not root:
                return None
            
            l = inorder(root.left)
            if l!=None:
                return l
            if self.k==1:
                return root.val
            self.k-=1
            return inorder(root.right)
        return inorder(root)
#         def helper(root,k):
#             if not root:
#                 return 0
            
#             left = helper(root.left,k)
#             if self.ans:
#                 return left+1
#             elif left+1 ==k:
#                 self.ans = root.val
#                 return k
#             right = helper(root.right,k-left-1)
#             return left+1+right
#         helper(root,k)
#         return self.ans