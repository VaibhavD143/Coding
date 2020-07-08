"""
To understand base:
take example
[8,5,2,3,4,6,7,9]
[3,2,4,5,7,6,9,8]

[3,9,20,15,7]
[9,3,15,20,7]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        ind = {val:i for i,val in enumerate(inorder)}
        def rec(ps,pe,base):
            if ps == pe:
                return TreeNode(preorder[ps])
            if ps>pe:
                return None
            
            root = TreeNode(preorder[ps])
            i = ind[preorder[ps]]   #position in inorder
            diff = i-base   #number of elements in left tree of root
            root.left = rec(ps+1,ps+diff,base)
            root.right = rec(ps+diff+1,pe,i+1)
            return root
        return rec(0,len(preorder)-1,0)