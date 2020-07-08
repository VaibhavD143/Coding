# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         def rec(root,head,troot):
            
#             if not troot:
#                 if not root and not head:
#                     return True
#                 if (not root) ^ (not head):
#                     return False
#                 if root.val == head.val:
#                     return rec(root.left,head.left,None) and rec(root.right,head.right,None)
#                 else:
#                     return False
#             if not root:
#                 return False
#             if root.val == troot.val and rec(root.left,troot.left,None) and rec(root.right,troot.right,None):
#                 return True
#             return rec(root.left,None,troot) or rec(root.right,None,troot)
#         return rec(s,None,t)
        def inorder(root):
            if not root:
                return '$'
            return F'^{root.val}#'+inorder(root.left)+inorder(root.right)
        
        return inorder(t) in inorder(s)