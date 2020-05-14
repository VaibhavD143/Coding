"""
Input:
tc = no of inputs
each line:
x y
where 	x = operation (i = insert, d = delete)
		y = value
"""

class node():
	"""docstring for node"""
	def __init__(self):
		self.left = None
		self.right = None
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

def find_in_suc(root):
	froot = root.right
	while froot.left:
		froot = froot.left

	suc = froot.val
	delete(root,suc)
	return suc


def delete(root,elm):

	if root.val == elm:
		if root.left == None:
			return root.right,1
		elif root.right == None:
			return root.left,1
		else:
			suc = find_in_suc(root)
			root.val = suc
			return root,1

	proot = None
	aroot = root
	ind = 1
	while 1:
		if root.val == None:
			#value not present
			return aroot,-1

		elif root.val > elm:
			#left subtree
			proot = root
			root = root.left
			ind = 2*ind

		elif root.val < elm:
			#right subtree
			proot = root
			root = root.right
			ind = 2*ind + 1

		elif root.left == None:
			#element found and has right child
			if proot.left is root:
				proot.left =root.right
			else:
				proot.right = root.right
			return aroot,ind

		elif root.right == None:
			#element found and has left child
			if proot.right is root:
				proot.right =root.left
			else:
				proot.left = root.left
			return aroot,ind

		else:
			#element found and have both children
			suc = find_in_suc(root)
			root.val = suc
			return aroot,ind



def insert(root,elm):
	ind = 1
	while 1:
		if root.val == None:
			root.val = elm
			root.ind = ind
			break
		elif root.val > elm:
			if not root.left:
				root.left = node()
				root.left.val = elm
				root.left.ind = 2*ind
				ind = 2*ind
				break
			root = root.left
			ind = 2*ind
		else:
			if not root.right:
				root.right = node()
				root.right.val = elm
				ind = 2*ind + 1
				break
			root = root.right
			ind = 2*ind + 1

	return ind

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



if __name__ == '__main__':

	# a = node()
	# fun(a)
	# print(vars(a))

	tc = int(input())
	root = node()
	while tc:
		
		op,val = input().strip().split()
		val=int(val)
		root.ind = 1
		if op == 'i':
			# root,ind = insert(root,val)
			ind = insert(root,val)
			print('----------------------------------------------------------------------')
			print(val,"In",ind)
			print2D(root)
		else:
			root,ind = delete(root,val)
			print('----------------------------------------------------------------------')
			print(val,"Del",ind)
			print2D(root)
		
		tc-=1