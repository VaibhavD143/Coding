"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left and not root.right:
            return root
        left = root.left
        right = root.right
        troot = root
        if not right:
            while troot.next:
                if troot.next.left:
                    left.next=troot.next.left
                    break
                elif troot.next.right:
                    left.next=troot.next.right
                    break
                troot=troot.next
        else:
            if left:
                left.next = right
            while troot.next:
                if troot.next.left:
                    right.next=troot.next.left
                    break
                elif troot.next.right:
                    right.next=troot.next.right
                    break
                troot=troot.next
        self.connect(right)
        self.connect(left)
        return root