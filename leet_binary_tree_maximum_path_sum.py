# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res =float('-inf')
        def dfs(root):
            if not root:
                return float('-inf')
            
            lsum = dfs(root.left)
            rsum = dfs(root.right)
            
            self.res = max(self.res,lsum,rsum,lsum+root.val+rsum)
            # print(self.res,max(root.val,root.val+lsum,root.val+rsum))
            return max(root.val,root.val+lsum,root.val+rsum)
        
        return max(dfs(root),self.res)

[-10,0,-1]
[-2,-1]
[1,-2,-3,1,3,-2,null,-1]