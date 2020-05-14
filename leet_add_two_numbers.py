# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        tres = res
        carry = 0
        while l1 and l2:
            sm = l1.val+l2.val+carry
            tres.val = sm%10
            sm = sm//10
            carry = sm
            l1 = l1.next
            l2 = l2.next
            tres.next = ListNode(0)
            tres = tres.next
        while l1:
            sm = l1.val+carry
            tres.val = sm%10
            sm = sm//10
            carry = sm
            l1 = l1.next
            tres.next = ListNode(0)
            tres = tres.next
        
        while l2:
            sm = l2.val+carry
            tres.val = sm%10
            sm = sm//10
            carry = sm
            l2 = l2.next
            tres.next = ListNode(0)
            tres = tres.next
        if carry > 0:
            tres.val = carry
            return res
        tres = res
        while tres.next:
            if not tres.next.next:
                tres.next = None
                break
            tres = tres.next
        return res