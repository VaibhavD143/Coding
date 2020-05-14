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

def insert(root,elm,ind):
	if root == None:
		root = node()
		root.val = elm
		print(ind)

	elif root.val > elm:
		root.left = insert(root.left,elm,2*ind)

	else:
		root.right = insert(root.right,elm,2*ind+1)

	return root

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
	
	else:
		if root.left == None:
			print(ind)
			return root.right
		elif root.right == None:
			print(ind)
			return root.left
		else:
			print(ind)
			suc = find_suc(root.right)
			root.right = delete(root.right,suc,2*ind+1)
			root.val = suc
			return root

	return root

if __name__ == '__main__':

	tc = int(input())
	root = None
	while tc:
		
		op,val = input().strip().split()
		val=int(val)
		ind = 1
		if op == 'i':
			root = insert(root,val,1)
			# print('---------------------------- in ',val,'----------------------------')	
			# print2D(root)
		else:
			root= delete(root,val,1)
			# print('---------------------------- del ',val,'----------------------------')	
			# print2D(root)
		tc-=1