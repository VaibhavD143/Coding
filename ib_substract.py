# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        
        slow = A
        fast = A.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        nex = slow.next
        while nex:
            nex.next,prev,nex = prev,nex,nex.next
        slow.next = prev
        
        head = A
        tail = prev
        while tail != None:
            head.val = tail.val-head.val
            head = head.next
            tail = tail.next
        
        prev = None
        nex = slow.next
        while nex:
            nex.next,prev,nex = prev,nex,nex.next
        slow.next = prev
        return A
        