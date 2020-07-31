# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # s1 = [root]
        # s2 = []
        # res = []
        # while s1:
        #     res.append(s1[0].val)
        #     s2 = []
        #     for u in s1:
        #         if u.right:
        #             s2.append(u.right)
        #         if u.left:
        #             s2.append(u.left)
        #     s1=s2
        def rec(root,level):
            if not root:
                return
            
            if len(res)<level:
                res.append(root.val)
            rec(root.right,level+1)
            rec(root.left,level+1)
            
        res = []
        rec(root,1)
        return res