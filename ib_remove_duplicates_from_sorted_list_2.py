Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, root):
        extra = ListNode('a')
        extra.next = root
        troot= extra
        while troot.next:
            flag=0
            while troot.next.next and troot.next.val == troot.next.next.val:
                flag = 1
                tmp = troot.next.next
                troot.next.next = tmp.next
                del tmp
            if flag:
                tmp = troot.next
                troot.next = tmp.next
                del tmp
            else:
                troot = troot.next
        return extra.next