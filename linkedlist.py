class Node:

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class LinkedList():
	
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		node = Node(data, self.head)
		self.head = node

	def print_ll(self):
		if self.head is None:
			print("LinkedList is empty")
		
		ll_str = ""
		iterator = self.head
		while iterator:
			ll_str += str(iterator.data) + " --> "
			iterator = iterator.next
		print(ll_str)

	def remove_from_front(self):
		if self.head is None:
			print("LinkedList is empty")
		self.head = self.head.next

	def insert_at_end(self, data):
		if self.head == None:
			self.head = Node(data, None)
		iterator = self.head
		while iterator.next:
			iterator = iterator.next
		if iterator.next == None:
			iterator.next = Node(data,None)

	def length(self):
		count = 0
		iterator = self.head
		while iterator:
			count = count+1
			iterator = iterator.next
		return count

	def remove_from_back(self):
		if self.head == None:
			print("LinkedList is empty")
		rear = self.head
		deletion_iterator = rear
		while rear:
			deletion_iterator = rear
			rear = rear.next
			if rear.next == None:
				rear = None
		if rear == self.head:
			self.head == None

			

if __name__ == "__main__":

	ll = LinkedList()
	ll.insert_at_beginning(5)
	# ll.insert_at_beginning(10)
	# ll.insert_at_beginning(15)
	# ll.insert_at_end(150)
	ll.insert_at_end(250)
	ll.print_ll()
	# ll.remove_from_front()
	# ll.print_ll()
	# ll.remove_from_front()
	# ll.print_ll()
	# ll.insert_at_end(200)
	# ll.insert_at_end(300)
	# ll.print_ll()
	ll.remove_from_back()
	ll.print_ll()
	ll.remove_from_back()
	ll.print_ll()
	ll.remove_from_back()
	ll.print_ll()
