# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        head = A
        k=B
        ss = []
        while head:
            ss.append(head)
            head=head.left
        while ss:
            node = ss.pop()
            k-=1
            if not k:
                return node.val
            if node.right:
                ss.append(node.right)
                node=node.right
                while node.left:
                    ss.append(node.left)
                    node=node.left