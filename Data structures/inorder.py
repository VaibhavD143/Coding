def inorder(root):
    stack = []
    node = root
    while node:
        stack.append(node)
        node = node.left
    while stack:
        node = stack.pop()
        print(node.val)
        right = node.right
        while right:
            stack.append(right)
            right = right.left