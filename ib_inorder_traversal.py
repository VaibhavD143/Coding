# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        head = A
        ss = []
        res=[]
        while head:
            ss.append(head)
            head=head.left
        while ss:
            node = ss.pop()
            res.append(node.val)
            if node.right:
                ss.append(node.right)
                node=node.right
                while node.left:
                    ss.append(node.left)
                    node=node.left
        return res