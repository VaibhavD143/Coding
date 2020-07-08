# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst =[]
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)
        inorder(root)
        def bst(start,end):
            if start>end:
                return None
            if start == end:
                return TreeNode(lst[start])
            
            mid = start+(end-start)//2
            root = TreeNode(lst[mid])
            root.left = bst(start,mid-1)
            root.right = bst(mid+1,end)
            return root
        return bst(0,len(lst)-1)
            