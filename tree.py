class tree_node:
	
	def __init__(self, data):
		self.data = data
		self.children = []
		self.parent = None

	def add_child(self, child):
		self.parent = self

		self.children.append(child)

	def tree_height(self):
		count = 0
		p = self.parent
		while p:
			count += 1
			p = p.parent
		print(self.parent)
		
		return count

	def print_tree(self):
		# print(self.tree_height()*" " + self.data)
		print(self.tree_height())		
		if self.children:
			for child in self.children:
				child.print_tree()


if __name__ == "__main__":

	root = tree_node("Electronics")
	
	TV = tree_node("Television")
	laptop = tree_node("Laptop")
	cellphone = tree_node("Cellphone")
	root.print_tree()
	root.add_child(TV)
	root.add_child(laptop)
	root.add_child(cellphone)
	
	TV.add_child(tree_node("Samsung"))
	TV.add_child(tree_node("Sony"))
	TV.add_child(tree_node("LG"))

	laptop.add_child(tree_node("Windows"))
	laptop.add_child(tree_node("Mac"))
	
	cellphone.add_child(tree_node("Apple"))
	cellphone.add_child(tree_node("Vivo"))
	cellphone.add_child(tree_node("MI"))

	# root.print_tree()
