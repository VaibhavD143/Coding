# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def driver(cur):
            if not cur.next:
                self.root = cur
            
            else:
                driver(cur.next)
                cur.next.next = cur
        if not head:
            return head
        self.root = None
        driver(head)
        head.next = None
        return self.root
