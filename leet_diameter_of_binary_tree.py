class node():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)
res = 0
def findDepth(root):
    global res
    if not root:
        return 0
    ldepth = findDepth(root.left)
    rdepth = findDepth(root.right)
    res = max(res,ldepth+rdepth)
    return max(ldepth,rdepth)+1
root = node(5)
print(root)
findDepth(root)
print(res)