"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
#         def rec(root):
#             curr = root
#             nex = root.next
            
#             while nex:
#                 if curr.child:
#                     head,end = rec(curr.child)
#                     curr.child = None
#                     head.prev = curr
#                     curr.next=head
#                     nex.prev = end
#                     end.next = nex
#                 curr = nex
#                 nex = nex.next
#             if curr.child:
#                 head,end = rec(curr.child)
#                 curr.child = None
#                 curr.next = head
#                 head.prev = curr
#                 curr = end
#             return root,curr
                
#         root,_ = rec(head)
        curr = head
        # nex = head.next
        tail = []
        while curr:
            
            if curr.child:
                tmp = curr.child
                curr.child = None
                if curr.next:
                    tail.append(curr.next)
                curr.next = tmp
                tmp.prev = curr
                curr = tmp
                continue
            if not curr.next and tail:
                curr.next = tail.pop()
                curr.next.prev = curr
            else:
                curr = curr.next
        root = head
        # res = []
        # while head:
        #     print(head.val,end=" ")
        #     res.append(head.val)
        #     head = head.next
        return root