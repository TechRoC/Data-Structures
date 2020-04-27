class node:
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None
		
class binarytree:
	def __init__(self):
		self.root = None

#Recursive Insert		
	def insert(self,value):
		new_node = node(value)
		if self.root is None:
			self.root = new_node
		else:
			self._insert(value,self.root)
	
	def _insert(self,value,cur_node):
		if value < cur_node.data:
			if cur_node.left is None:
				cur_node.left = node(value)
			else:
				self._insert(value,cur_node.left)
		elif value > cur_node.data:
			if cur_node.right is None:
				cur_node.right = node(value)
			else:
				self._insert(value,cur_node.right)
		else:
			print("something went wrong")

# Non Recursive approach to insert the element		
	def levelordInsert(self,value):
		import queue
		q = queue.Queue()
		new_node = node(value)
		if self.root is None:
			self.root = new_node
		q.put(self.root)
		while not q.empty():
			cur = q.get()
			if new_node.data < cur.data:
				if cur.left is not None:
					q.put(cur.left)
				else:
					cur.left = new_node
			elif new_node.data > cur.data:
				if cur.right is not None:
					q.put(cur.right)
				else:
					cur.right = new_node
			
	def printt(self):
		if self.root != None:
			self._printtt(self.root)
			
	def _printtt(self,cur_node):
		if cur_node is not None:
			self._printtt(cur_node.left)
			print(cur_node.data)
			self._printtt(cur_node.right)

#preorder traverse			
	def preorder(self):
		cur_node = self.root
		stack = []
		result = []
		if cur_node:
			stack.append(cur_node)
		while stack:
			node = stack.pop()
			result.append(node.data)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		return result

#inorder traverse		
	def inorder(self):
		stack = []
		result = []	
		cur_node = self.root
		while stack or cur_node:
			if cur_node:
				stack.append(cur_node)
				cur_node = cur_node.left
			else:
				node = stack.pop()
				result.append(node.data)
				node = node.right
				if node != None:
					stack.append(node)
		return result

#level-order traverse	
	def levelorder(self):
		node = None
		cur_node = self.root
		stack = []
		import queue
		q = queue.Queue()
		q.put(cur_node)
		while not q.empty():
			node = q.get()
			stack.append(node.data)
			if node.left is not None:
				q.put(node.left)
			if node.right is not None:
				q.put(node.right)
		return stack
		
		
#Recursive approach to achieve the height of a tree			
	def height(self):
		cur_node= self.root
		if cur_node is None:
			return 0
		else:
			return self._height(cur_node,0)
	
	def _height(self,cur_node,heg):
		if cur_node == None:
			return heg
		data1 = self._height(cur_node.left,heg+1)
		data2 = self._height(cur_node.right,heg+1)
		return max(data1, data2)

#Diameter of a tree	
	def diameter(self,value):
		if value is None:
			return 0
		abc = self.heg(value.left)+ self.heg(value.right) 
		ldiameter = self.diameter(value.left)
		rdiameter = self.diameter(value.right)
		return max(abc,max(ldiameter,rdiameter))
	
	def heg(self,value):
		if value == None:
			return 0
		le = self.heg(value.left)
		rg = self.heg(value.right)
		return 1 + max(le ,rg)
	



#Count the number of element in a tree	
	def Count(self):
		temp = None
		import queue
		q = queue.Queue()
		cur_node = self.root
		q.put(cur_node)
		count = 0
		while not q.empty():
			temp = q.get()
			if temp.left is not None:
				count +=1
				q.put(temp.left)
			if temp.right is not None:
				count += 1
				q.put(temp.right)
		return count + 1



#search element in a tree	
	def search(self,value):
		cur_node = self.root
		import queue
		q = queue.Queue()
		q.put(cur_node)
		while not q.empty():
			node = q.get()			
			if value == node.data:
				return "found"
			if node.left is not None:
				q.put(node.left)
			if node.right is not None:
				q.put(node.right)
		return "not found"

#Display reverse tree data
	def reverse(self):
		stack1= []
		stack = []
		import queue
		q= queue.Queue()
		cur_node = self.root
		q.put(cur_node)
		while not q.empty():
			temp = q.get()
			stack.append(temp.data)
			if temp.left is not None:
				q.put(temp.left)
			if temp.right is not None:
				q.put(temp.right)
		while stack:
			stack1.append(stack.pop())
		return stack1
	
	
#Number of leaf node in a tree	
	def leafnode(self):
		stack = []
		import queue
		q = queue.Queue()
		q.put(self.root)
		count = 0
		while not q.empty():
			temp = q.get()
			if temp.left is None and temp.right is None:
				count +=1
				stack.append(temp.data)
			if temp.left is not None:
				q.put(temp.left)
			if temp.right is not None:
				q.put(temp.right)
		return count,stack

#Full nodes	
	def twochild(self):
		stack =[]
		import queue
		q = queue.Queue()
		q.put(self.root)
		count = 0
		while not q.empty():
			temp = q.get()
			if temp.left is not None and temp.right is not None:
				count +=1
				stack.append(temp.data)
			if temp.left is not None:
				q.put(temp.left)
			if temp.right is not None:
				q.put(temp.right)
		return count,stack
	
#half nodes	
	def onechild(self):
		stack =[]
		import queue
		q = queue.Queue()
		q.put(self.root)
		count = 0
		while not q.empty():
			temp = q.get()
			if (temp.left is None and temp.right is  not None) or (temp.left is not None and temp.right is None):
				count +=1
				stack.append(temp.data)
			if temp.left is not None:
				q.put(temp.left)
			if temp.right is not None:
				q.put(temp.right)
		return count,stack

			
tree = binarytree()
tree.levelordInsert(10)
tree.levelordInsert(12)
tree.levelordInsert(11)
tree.levelordInsert(13)
tree.levelordInsert(8)
tree.levelordInsert(9)
tree.levelordInsert(7)
tree.levelordInsert(6)
tree.levelordInsert(14)
print("Display is preorder :",tree.preorder())
print("Display in inorder :",tree.inorder())
print("Display in levelorder :",tree.levelorder())
print("height of tree :",tree.height())
print("Diameter of the tree :",tree.diameter(tree.root))
print("number of elements in tree :", tree.Count())
value,data = tree.leafnode()
print("there are {0} leaf nodes in a tree : {1}".format(value,data))
value1,data1= tree.twochild()
print("there are {0} elements with full nodes :{1}".format(value1,data1))
value2,data2 = tree.onechild()
print("there are {0} elements with half nodes : {1}".format(value2,data2))
