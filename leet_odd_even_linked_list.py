# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # pre = None
        odd = head
        half = head.next
        even = head.next
        # while even.next and even.next.next:
        while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
        
        # if even.next:
        #     odd.next = even.next
        #     odd = odd.next
        #     even.next = None
        odd.next = half
            
        return head