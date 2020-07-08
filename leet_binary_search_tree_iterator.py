# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ss=[]
        if root:
            self.ss.append(root)
            node = self.ss[-1]
            while node.left:
                self.ss.append(node.left)
                node=node.left
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.hasNext():
            return 
        node = self.ss.pop()
        if node.right:
            self.ss.append(node.right)
            curr = node.right
            while curr.left:
                self.ss.append(curr.left)
                curr=curr.left
        return node.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if not self.ss:
            return False
        return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()