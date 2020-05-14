class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root


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

from collections import deque

root = deserialize('[1,2,3,4,5,6]')
x = 1
y = 6
print2D(root)
ss =deque([root,-1])
firstFound =0
while len(ss)>1:
    node = ss.popleft()
    if node == -1:
        ss.append(-1)
        continue
    if node.left and node.left.val ==x or node.right and node.right.val ==x:
        firstFound =1
    if node.left and node.left.val ==y or node.right and node.right.val ==y:
        if firstFound == 1:
            print("same parent bc")
            exit(1)
        else:
            firstFound =1
            x,y= y,x
    if firstFound ==1:
        break
    if node.left:
        ss.append(node.left)
    if node.right:
        ss.append(node.right)

while ss[0]!=-1:
    node = ss.popleft()
    if node.left and node.left.val ==y or node.right and node.right.val ==y:
        print("found in layer bc")
        exit(1)
print("hard luck")