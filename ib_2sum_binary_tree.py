# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, root, B):
        if not root:
            return 0
        ss1 = []
        ss2 = []
        node = root
        while node:
            ss1.append(node)
            node=node.left
        node = root
        while node:
            ss2.append(node)
            node=node.right
        # ss1[-1].val<ss2[-1].val is to stop when both element meets at a point, as duplicates are not there and 2X = Y is not allowed            
        while ss1 and ss2 and ss1[-1].val<ss2[-1].val:
            if ss1[-1].val+ss2[-1].val < B:
                node = ss1.pop()
                node=node.right
                if node:
                    ss1.append(node)
                    while ss1[-1].left:
                        ss1.append(ss1[-1].left)
            elif ss1[-1].val+ss2[-1].val > B:
                node = ss2.pop()
                node= node.left
                if node:
                    ss2.append(node)
                    while ss2[-1].right:
                        ss2.append(ss2[-1].right)
            else:
                return 1
        return 0
            
            