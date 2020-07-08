from collections import deque
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        
        ss = deque([A,None])
        res = []
        tmp=[]
        flag = 1
        while ss:
            node = ss.popleft()
            if not node:
                if len(ss):
                    ss.append(None)
                res.append(tmp if flag else tmp[::-1])
                tmp=[]
                flag = 1-flag
                continue
            tmp.append(node.val)
            if node.left:
                ss.append(node.left)
            if node.right:
                ss.append(node.right)
        return res