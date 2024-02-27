class BinaryTreeNode:
	
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

	def add_child(self, child_data):

		if self.data == child_data:
			return 
		
		#Left subtree
		if self.data > child_data:

			if self.left:
				self.left.add_child(child_data)
			else:
				self.left = BinaryTreeNode(child_data)
		
		#Right subtree
		else:

			if self.right:
				self.right.add_child(child_data)
			else:
				self.right = BinaryTreeNode(child_data)


#######################################################################

	def inOrder_traversal(self):

		elements = []
		
		# Visit left subtree
		if self.left:
			elements += self.left.inOrder_traversal()

		# Visit node 
		elements.append(self.data)

		# Visit right subtree
		if self.right:
			elements += self.right.inOrder_traversal()

		return elements



	# def inOrder_traversal(self, tree, elements=[]):

	# 	if tree is not None:
	# 		print(tree.data)
	# 		self.inOrder_traversal(tree.left, elements)
	# 		elements.append(tree.data)
	# 		self.inOrder_traversal(tree.right, elements)

	# 	return elements

#######################################################################
	# def PreOrder_traversal(self, tree, elements=[]):

	# 	if tree is not None:
	# 		elements.append(tree.data)
	# 		self.PreOrder_traversal(tree.left, elements)
	# 		self.PreOrder_traversal(tree.right, elements)
	# 	return elements


	def PreOrder_traversal(self, elements=[]):

		if self is not None:
			elements.append(self.data)
			if self.left is not None:
				self.left.PreOrder_traversal(elements)
			if self.right is not None:
				self.right.PreOrder_traversal(elements)
		return elements

##########################################################################

	def PostOrder_traversal(self, elements=[]):
		if self:
			if self.left:
				self.left.PostOrder_traversal(elements)
			if self.right:	
				self.right.PostOrder_traversal(elements)
			elements.append(self.data)
		return elements


#######################################################################


if __name__ == "__main__":


		tree_list = [18,4,1,63,23,7,1,6]
		data = tree_list[0]
		root = BinaryTreeNode(data)
		
		# Inserting nodes
		for i in range(1,len(tree_list)):
			root.add_child(tree_list[i])

		# Print Tree (inorder traversal method 1)	
		element = root.inOrder_traversal()
		print("InOrder traversal: ", element)

		# Print Tree (inorder traversal method 2)	
		# element = root.inOrder_traversal(root)
		# print(element)


		# # Print Tree (PreOrder traversal method 1)	
		# element = root.PreOrder_traversal(root)
		# print(element)

		# Print Tree (PreOrder traversal method 2)	
		element = root.PreOrder_traversal()
		print("PreOrder traversal: ", element)


		# Print Tree (PostOrder traversal method 2)	
		element = root.PostOrder_traversal()
		print("PostOrder traversal: ", element)



