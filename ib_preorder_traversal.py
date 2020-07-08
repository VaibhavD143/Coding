# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        head = A
        ss = []
        res=[]
        while head:
            ss.append(head)
            res.append(head.val)
            head=head.left
        while ss:
            node = ss.pop()
            if node.right:
                ss.append(node.right)
                res.append(node.right.val)
                node=node.right
                while node.left:
                    ss.append(node.left)
                    res.append(node.left.val)
                    node=node.left
        return res