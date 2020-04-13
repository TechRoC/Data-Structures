class node:
	def __init__(self,prev=None,next=None,data=None):
		self.data = data
		self.next = next
		self.prev = prev

class doublelinklist:
	def __init__(self):
		self.head = None
	
	def prepend(self,new_data):
		new_node = node(data = new_data)
		if self.head is None:
			self.head = new_node
			new_node.next = None
			new_node.prev = None
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
			new_node.prev = None
	
	def append(self,new_data):
		new_node = node(data=new_data)
		if self.head is None:
			self.head = new_node
			new_node.next = None
			new_node.prev = None
		else:
			cur = self.head
			while cur.next != None:
				cur = cur.next
			cur.next = new_node
			new_node.prev = cur
			new_node.next = None
	
	def after(self,prev_data,new_data):
		new_node = node(data=new_data)
		temp = None
		if self.head == prev_data:
			temp = self.head.next
			new_node.next = temp
			temp.prev = new_node
			self.head.next = new_node
			new_node.prev = self.head
		cur = self.head
		while cur.next !=None:
			cur = cur.next
			if cur == prev_data:
				temp = cur.next
				new_node.next = temp
				temp.prev = new_node
				cur.next = new_node
				new_node.prev = cur
	
	def remove(self,value):
		temp = None
		temp1 = None
		if self.head.data == value:
			temp = self.head.next
			self.head = temp 
			temp.prev = None
		else:
			cur = self.head
			while cur.next != None:
				cur = cur.next
				if cur.data == value:
					temp = cur.prev
					temp1 = cur.next
					temp.next = temp1
					temp1.prev = temp
					
	def find(self,value):
		cur = self.head
		count = 0
		while cur:
			if cur.data == value:
				print("found at {0} position".format(count))
	
			elif cur.next is None and cur.data !=value:
				return False
			cur = cur.next
			count += 1
				
					
					
	def sorted_insert(self,new_data):
		new_node = node(data = new_data)
		temp = None
		temp1 = None
		cur = self.head
		while cur:
			if new_node.data > cur.data:
				if cur.next == None:
					temp = cur
					temp1 = new_node
					temp.next = temp1
					temp1.next = None
					temp1.prev = temp
					break
				cur = cur.next
			else:
				if new_node.data < cur.data:
					if new_node.data < self.head.data:
						self.prepend(new_data)
						break
					else:
						self.after(cur.prev,new_data)
						break
						
	def len(self):
		count = 0
		cur = self.head
		while cur:
			count += 1
			cur = cur.next
			if cur == None:
				break
		return count
					
	def printt(self):
		cur = self.head
		ele =[]
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print(ele)

list = doublelinklist()
list.prepend(1)
list.sorted_insert(2)
list.sorted_insert(4)
list.sorted_insert(0)
list.sorted_insert(3)
list.sorted_insert(7)
list.sorted_insert(15)
list.after(list.head.next.next,5)
list.printt()
list.remove(0)
list.remove(7)
list.printt()
list.swap(4,3)
		