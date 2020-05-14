def isBST(root):
    # Code here
    print(check_bst(root,0,1001))
        
def check_bst(root,l,r):
    if root.data <= l:
        return 0
    left_val =1
    right_val = 1
    if root.left:
    left_val = check_bst(root.left,l,root.data)
    if root.right:
    right_val = check_bst(root.right,root.data,r)

    return left_val&right_val