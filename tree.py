
class Tree(object):
	"""docstring for Tree"""
	def __init__(self ):
		super(Tree, self).__init__()
		self.data = {}
	
	def add(self,name,value):
		self.name = Tree()
		self.data[name] = value

	def get_childrens(self):
		return self.data

if __name__ == '__main__':
	my_tree = Tree()
	my_tree.add('left',5)
	my_tree.add('right',10)
	print(my_tree.get_childrens())