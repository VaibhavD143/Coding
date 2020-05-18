"""
gyaan : 
how to detect first node of cycle
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, root):
        if not root or not root.next:
            return None
        slow,fast = root,root
        #this step is because initially both are starting from root, that's why
        #initial position of slow,fast decides while condition.
        slow = slow.next
        fast = fast.next.next
        flag = 0
        while fast and fast.next:
            if slow == fast:
                flag =1
                break
            slow = slow.next
            fast = fast.next.next
        if not flag:
            return None
        slow = root
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow
        # ha = {}
        # while root:
        #     # print(ha)
        #     if root in ha:
        #         return root
        #     ha[root]=root.val
        #     root = root.next
        