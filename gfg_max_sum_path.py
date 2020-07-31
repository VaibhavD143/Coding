def maxPathSum(root):
    # code here 
    def rec(root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.data
        if not root.left:
            return root.data+rec(root.right)
        if not root.right:
            return root.data+rec(root.left)
        nonlocal res
        left = rec(root.left)
        right = rec(root.right)
        res  = max(res,left+root.data+right)
        return max(left,right)+root.data
    res = float('-inf')
    rec(root)
    return res
