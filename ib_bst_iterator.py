# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.ss=[]
        if root:
            self.ss.append(root)
            node = self.ss[-1]
            while node.left:
                self.ss.append(node.left)
                node=node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if not self.ss:
            return False
        return True

    # @return an integer, the next smallest number
    def next(self):
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

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
