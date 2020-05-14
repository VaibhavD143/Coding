# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        r = head
        f = head.next
        while f and f.next:
            tf = f
            tr = r
            while tf.next:
                tr = tf
                tf = tf.next
            r.next = tf
            tf.next = f
            tr.next = None
            r = f
            f = f.next

