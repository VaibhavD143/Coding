class node():
	"""docstring for node"""
	def __init__(self):
		self.left = None
		self.right = None
		self.back = None
		self.val=None
		self.ind=None

COUNT = [10]
def print2DUtil(root, space) : 
	# Base case 
	if (root == None) : 
		return

	# Increase distance between levels 
	space += COUNT[0] 

	# Process right child first 
	print2DUtil(root.right, space) 

	# Print current node after space 
	# count 
	print() 
	for i in range(COUNT[0], space): 
		print(end = " ") 
	print(root.val) 

	# Process left child 
	print2DUtil(root.left, space) 

# Wrapper over print2DUtil() 
def print2D(root) : 
	
	# space=[0] 
	# Pass initial space count as 0 
	print2DUtil(root, 0) 

# def insert(root,elm,ind):
# 	if root == None:
# 		root = node()
# 		root.val = elm
# 		print(ind)

# 	elif root.val > elm:
# 		root.left = insert(root.left,elm,2*ind)
# 		root.left.back = root

# 	else:
# 		root.right = insert(root.right,elm,2*ind+1)
# 		root.right.back = root

# 	return root


def find_suc(root):

	while root.left:
		root = root.left

	return root.val



def delete(root,elm,ind):
    if root == None:
        return None

    elif root.val > elm:
        root.left = delete(root.left,elm,2*ind)

    elif root.val < elm:
        root.right = delete(root.right,elm,2*ind+1)

    elif (root.left == None and root.right == None):
        print(ind)
        return None
    elif root.left == None:
        print(ind)
        root.right.back = root.back
        return root.right
    elif root.right == None:
        print(ind)
        root.left.back = root.back
        return root.left
    else:
        print(ind)
        suc = find_suc(root.right)
        root.right = delete(root.right,suc,2*ind+1)
        root.val = suc
        return root

    return root

def find_ind(root,x):
	if root.val == x:
		return root
	elif root.val > x:
		return find_ind(root.left,x) if root.left else None
	else:
		return find_ind(root.right,x) if root.right else None

def successor(root,x):
	root = find_ind(root,x)
	if root:
		if root.right:
			root = root.right
			while root.left:
				root = root.left
			return root.val
		elif root.back and root.back.left == root:
			return root.back.val
		else:
			while root.back and root.back.right == root:
				root= root.back
			return root.back.val if root.back and root.back.left == root else "No successor"
	return "Element not found"

def predecessor(root,x):
	root = find_ind(root,x)
	if root:
		if root.left:
			root = root.left
			while root.right:
				root = root.right
			return root.val
		elif root.back and root.back.right == root:
			return root.back.val
		else:
			while root.back and root.back.left == root:
				root = root.back
			return root.back.val if root.back and root.back.right == root else "No predecessor"
	return "Element not found"

def insert(root,elm,ind):
    if root.val > elm:
        if root.left == None:
            root.left = node()
            root.left.val = elm
            root.left.back = root
            root.left.ind = 2*ind
            print(root.left.ind)
        else:
            root.left = insert(root.left,elm,2*ind)
    else:
        if root.right == None:
            root.right = node()
            root.right.val = elm
            root.right.back = root
            root.right.ind = 2*ind+1
            print(root.right.ind)
        else:
            root.right = insert(root.right,elm,2*ind+1)
    return root

if __name__ == '__main__':
    root = node()
    root.val = 50
    lst = [25,75,60,10,30]
    for i in lst:
        root = insert(root,i,1)
        print2D(root)
        print("----------------------")

    root = delete(root,60,1)
    print2D(root)
    print(root.right.left)
    # print2D(root)