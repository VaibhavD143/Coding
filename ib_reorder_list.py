# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, head):
        if not head or not head.next:
            return head
        #Find center
        #If odd then slow will stop at center
        #If even then on right side
        slow=head
        fast=head
        cnt=1
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            cnt+=2

        #When list is even and fast pointer goes out of linked list
        if fast == None:
            cnt-=1
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
        # print(cnt)
        #if odd then center element is already pointing to None, so floor value
        if cnt&1:
            cnt=cnt//2
        #if even then left of center is pointing to right and right of center is pointing to None so no need to touch them
        else:
            cnt=cnt//2-1
        while cnt:
            startNext = start.next
            tailNext = tail.next
            start.next = tail
            tail.next = startNext
            tail = tailNext
            start = startNext
            cnt-=1
        return head