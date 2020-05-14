# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def driver(cur):
            pre = None
            while cur:
                tmp = cur
                cur = cur.next
                tmp.next = pre
                pre = tmp
            return pre   
        if not head:
            return head
        return driver(head)
        
