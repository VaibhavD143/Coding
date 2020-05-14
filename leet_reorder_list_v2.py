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
        thead = head
        st = []
        l = 0
        r = -1 #index of right side
        while thead:
            st.append(thead)
            thead = thead.next
            r+=1

        while l<r-1:
            thead = st[l]
            st[r].next = thead.next
            thead.next = st[r]
            st[r-1].next = None
            l+=1
            r-=1
        