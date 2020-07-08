# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, root):
        prev = None
        fault = [None,None]
        def inOrder(root):
            if not root:
                return None
            nonlocal prev  
            nonlocal fault
            inOrder(root.left)
            
            if prev is not None and prev>root.val:
                if fault[0] != None:
                    fault[1]=root.val
                else:
                    fault = [prev,root.val]
            prev = root.val
            inOrder(root.right)
        inOrder(root)
        fault.sort()
        return fault