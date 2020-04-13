class node:
	def __init__(self,data):
		self.data = data
		self.next = None

class circularlist:
	def __init__(self):
		self.head = None
		
	def prepend(self,data):
		new_node = node(data)
		cur = self.head
		new_node.next = self.head
		if not self.head:
			self.head = new_node
			new_node.next = self.head
		else:
			while cur.next != self.head:
				cur = cur.next
			cur.next = new_node
			self.head = new_node
	
	def append(self,data):
		new_node = node(data)
		if not self.head:
			self.head = new_node
			new_node.next = self.head
		else:
			cur = self.head
			while cur.next != self.head:
				cur = cur.next
			cur.next = new_node
			new_node.next = self.head
	
	def remove(self,value):
		if self.head.data == value:
			cur = self.head
			while cur.next != self.head:
				cur = cur.next
			cur.next = self.head.next
			self.head = self.head.next
		else:
			cur = self.head
			prev = None
			while cur.next != self.head:
				pre = cur
				cur = cur.next
				if cur.data == value:
					pre.next = cur.next
					cur = cur.next
					
	def after(self,pre,data):
		 new_node = node(data)
		 if self.head == pre:
		 	new_node.next = self.head.next
		 	self.head.next = new_node
		 else:
		 	cur = self.head
		 	while cur.next != self.head:
		 		cur = cur.next
		 		if cur == pre:
		 			new_node.next = cur.next
		 			cur.next = new_node
		 			
	def __len__(self):
		cur = self.head
		total = 0
		while cur:
			total += 1
			cur = cur.next
			if cur == self.head:
				break
		return total
	
	def split(self):
		size = len(self)
		if size == 0:
			return None
		if size == 1:
			return self.head
		cur = self.head
		temp = None
		count = 0
		mid = size // 2
		while cur and count<mid:
			temp = cur 
			cur = cur.next
			count +=1
		temp.next = self.head
		splity = circularlist()
		while cur.next != self.head:
			splity.append(cur.data)
			cur = cur.next
		splity.append(cur.data)
		self.printt()
		splity.printt()
						
	def printt(self):
		cur = self.head
		ele = []
		while cur:
			ele.append(cur.data)
			cur = cur.next
			if cur == self.head:
				break
		print(ele)

list = circularlist()
list.append(1)
list.append(2)
list.append(3)
list.append(5)
list.printt()
list.split()