# Definition for a  binary tree node
class TreeNode:

    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right =None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        # print(A,B)
        if not A:
            return None
        if len(A)==1:
            return TreeNode(A[0])
        
        root = TreeNode(B[-1])
        left = 0
        while left<len(A) and A[left]!=B[-1]:
            left+=1
        root.left = self.buildTree(A[:left],B[:left])
        root.right = self.buildTree(A[left+1:],B[left:len(B)-1])
        return root