

#링크드리스트

class Node:
  def __init__(self,data,next=None):
    self.data = data
    self.next = next

node1 = Node(1)
node2 = Node(2)
node1.next = node2 #연결해줌
head = node1

def add(data):
  node = head
  while node.next:
    node = node.next
  node.next = Node(data)

node1 = Node(1)
head = node1
for index in range(2,10):
  add(index)

node = head
while node.next:
  print(node.data)
  node = node.next
print(node.data)

node = head
node3 = Node(1.5)
search = True
while search:
  if node.data == 1:
    search = False
  else:
    node = node.next
next_node = node.next
node.next = node3
node3.next = next_node

node = head
while node.next:
  print(node.data)
  node = node.next
print(node.data)




class Node:
  def __init__(self,data,next=None):
    self.data = data
    self.next = next

class NodeMgmt:
  def __init__(self,data):
    self.head = Node(data)
  def add(self,data):
    if self.head == '':
      self.head = Node(data)
    else:
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(data)

  def desc(self):
    node = self.head
    while node.next:
      print(node.data)
      node = node.next
    print(node.data)

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()

for data in range(1,10):
  linkedlist1.add(data)
linkedlist1.desc()


