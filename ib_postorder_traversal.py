# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        ss=[[A,1]]
        res = []
        while ss:
            node,val = ss.pop()
            if val ==0:
                res.append(node.val)
                continue
            ss.append([node,0])
            if node.right:
                ss.append([node.right,1])
            if node.left:
                ss.append([node.left,1])
        return res