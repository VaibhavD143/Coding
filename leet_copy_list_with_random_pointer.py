class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def pp(root):
    while root:
        print(root.val,end=" ")
        root=root.next
    print()

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        newHead = Node(head.val)
        ha = {head:newHead}
        thead = head.next
        tnewHead = newHead
        while thead:
            tnode = Node(thead.val)
            tnewHead.next = tnode
            tnewHead = tnewHead.next
            ha[thead] = tnewHead
            thead = thead.next 
        thead = head
        tnewHead = newHead
        # print(t.val,newHead.val)
        # return tnewHead
        while thead and tnewHead:
            tnewHead.random = ha[thead.random] if thead.random else None
            thead = thead.next
            tnewHead = tnewHead.next
        # print(head.val,head.next.val)
        return newHead