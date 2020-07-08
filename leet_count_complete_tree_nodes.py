# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root) -> int:
        # if not root:
        #     return 0
        # return self.countNodes(root.left)+self.countNodes(root.right)+1
        
        if not root:
            return 0
    
        if not root.left:
            return 1
        
        #is binary path exist
        def probe(root, path):
            node = root
            for p in path:
                node = node.left if p == '0' else node.right
            return node != None
        
        #binary path
        def bp(num, d):
            p = bin(num)[2:]
            return (d-1-len(p))*'0'+p
        
        d = 1
        node = root
        while node.left:
            node = node.left
            d += 1
        
        l, r = 0, 2**(d-1)-1
        while l < r:
            p = (l+r)//2
            if not probe(root, bp(p, d)):
                r = p-1
            else:
                l = p+1
        if probe(root, bp(r, d)):
            return r+2**(d-1)
        else:
            return r+2**(d-1)-1