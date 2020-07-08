# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, head):
        #Find center
        #If odd then slow will stop at center
        #If even then on right side
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #Reverse after center
        prev = None
        curr = slow
        nex = slow.next
        while nex:
            curr.next = prev
            prev = curr
            curr=nex
            nex = nex.next
        curr.next = prev
        tail = curr
        start = head
        #If odd then center will point to None and right side will point to center
        #If even then right of center will point to None
        while start and tail:
            if start.val != tail.val:
                return 0
            start,tail = start.next,tail.next
        return 1
        
        
        
        