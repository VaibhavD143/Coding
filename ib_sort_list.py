from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, root):
        if not root:
            return None
        def mergeSort(root):
            if not root.next:
                return root
            slow = root
            fast = root.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            slow.next,slow = None,slow.next
            
            left = mergeSort(root)
            right = mergeSort(slow)
            root = merge(left,right)
            # p(root)
            return root
                
        def merge(left,right):
            if left.val>right.val:
                left,right = right,left
            root = head = left
            left = left.next
            while left and right:
                if left.val < right.val:
                    head.next = left
                    left = left.next
                else:
                    head.next = right
                    right = right.next
                head = head.next
            if left:
                head.next = left
            if right:
                head.next = right
            return root
        def p(root):
            if not root:
                print()
                return
            print(root.val,end=" ")
            p(root.next)
        return mergeSort(root)