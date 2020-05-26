# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # def bs(lst,target):
        #     low=0
        #     high=len(lst)
        #     while low<high:
        #         mid = low+(high-low)//2
        #         if lst[mid] == target:
        #             return mid
        #         if lst[mid]<target:
        #             low=mid+1
        #         else:
        #             high=mid
        #     return low
        if not len(preorder):
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        part=1
        while part<len(preorder) and preorder[part]<preorder[0]:
            part+=1
        root.left = self.bstFromPreorder(preorder[1:part])
        root.right = self.bstFromPreorder(preorder[part:])
        return root
