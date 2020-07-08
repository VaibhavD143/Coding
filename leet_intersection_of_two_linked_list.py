# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1 = headA
        node2 = headB
        cnt=0
        while node1 and node2:
            cnt+=1
            node1= node1.next
            node2 =node2.next
        diff = 0
        if node1:
            while node1:
                node1=node1.next
                diff+=1
            node1=headA
            while diff:
                node1=node1.next
                diff-=1
            node2=headB
        elif node2:
            while node2:
                node2= node2.next
                diff+=1
            node2 = headB
            while diff:
                node2=node2.next
                diff-=1
            node1 = headA
        else:
            node1 = headA
            node2 = headB
        
        while not (node1 is node2):
            node1=node1.next
            node2=node2.next
        return node1
        