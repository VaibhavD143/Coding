# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root or not root.left and not root.right:
            return
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

#EDITORIAL
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        node = root
        while node:
            lstart = node
            foundFirst = False
            prev = None
            while lstart:
                if lstart.left : 
                    if not foundFirst:
                        foundFirst = True
                        node = lstart.left 
                        prev= lstart.left
                    else:
                        prev.next = lstart.left
                        prev = lstart.left
                if lstart.right :
                    if not foundFirst :
                        foundFirst = True
                        node = lstart.right 
                        prev= lstart.right
                    else:
                        prev.next = lstart.right
                        prev = lstart.right
                lstart = lstart.next
            if not foundFirst:
                node = None
        return root