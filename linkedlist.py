class SList:
	def __init__(self):
		self.head = None
	def add_to_front(self, val):
		new_node = SLNode(val)
		current_head = self.head
		new_node.next = current_head
		self.head = new_node
		return self

	def removeNode(self, val):
		runner = self.head
		if runner is not None:
			if runner.value == val:
				self.head = runner.next
				return self
		while runner is not None:
			if runner.value == val:
				break
			prev = runner
			runner = runner.next  
		if runner == None:
			return
		prev.next = runner.next
		return self


	def add_to_back(self, val):
		if self.head == None:
			self.add_to_front(val)
			return self
		new_node = SLNode(val)
		runner = self.head
		while (runner.next != None):
			runner = runner.next
		runner.next = new_node
		return self

	def print_values(self):
		runner = self.head
		while (runner != None):
			print(runner.value)
			runner = runner.next
		return self

class SLNode:
	def __init__(self, val):
		self.value = val
		self.next = None

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
my_list.add_to_back("Just").add_to_back("Kidding").print_values()
my_list.removeNode("Just").print_values()
