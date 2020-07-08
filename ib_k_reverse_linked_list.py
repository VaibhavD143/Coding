# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        head = A
        prev = None
        curr = A
        cnt=B
        #getting our root pointer to return to
        while cnt and curr:
            curr.next,prev,curr = prev,curr,curr.next
            cnt-=1
        root = prev
        head.next = curr
        while curr:
            cnt=B
            prev = head
            prevTail = head 
            head =curr  
            while cnt:
                curr.next , prev,curr = prev,curr,curr.next
                cnt-=1
            prevTail.next = prev    #to attach tail of last reversed linked list with head of current list
            head.next = curr        #keeping a tail of current linked list after reversing it
        return root
            
            
            
            