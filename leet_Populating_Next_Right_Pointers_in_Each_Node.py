# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        troot = root
        left = self.connect(troot.left)
        right = self.connect(troot.right)
        while left:
            left.next = right
            left=left.right
            right=right.left
        return root