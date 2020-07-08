# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
#         def rec(tree,link):
#             if not link:
#                 return True
#             if not tree:
#                 return False
            
#             if (tree,link) in ha:
#                 return False
            
#             nonlocal head
            
#             if tree.val == link.val and (rec(tree.left,link.next) or rec(tree.right,link.next)):
#                 return True
                    
#             res = (rec(tree.left,head) or rec(tree.right,head))
#             if not res:
#                 ha.add((tree,link))
#             return res
#         ha = set()
#         return rec(root,head)
        ll,lps = [head.val],[0]
        node = head.next
        length = 0
        while node:        
            if node.val == ll[length]:
                length+=1
                lps.append(length)
                ll.append(node.val)
                node = node.next
            else:
                if length!=0:
                    length = lps[length-1]
                else:
                    lps.append(length)
                    ll.append(node.val)
                    node = node.next
        def dfs(root,ind):
            if ind == len(ll):
                return True
            if not root:
                return False
            while ind and root.val != ll[ind]:
                ind = lps[ind-1]
                
            return dfs(root.left,ind+1) or dfs(root.right,ind+1)
        
        return dfs(root,0)