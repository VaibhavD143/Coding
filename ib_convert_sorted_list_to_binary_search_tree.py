# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def sortedListToBST(self, A):
        if not A:
            return None
        if not A.next:
            return TreeNode(A.val)
            
        root =A
        prev,slow,fast = None,A,A
        
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        
        prev.next = None
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(root)
        node.right = self.sortedListToBST(slow.next)
        return node
    
        