class Node:
  def __init__(self,data,prev=None,next=None):
    self.prev = prev
    self.next = next
    self.data = data

class NodeMgmt:
  def __init__(self,data):
    self.head = Node(data)
    self.tail = self.head # 처음 노드가 하나일때는 head ,tail 동일

  def insert(self,data):
    if self.head == None:
      self.head = Node(data)
      self.tail = Node(data)
    else:
      node = self.head
      while node.next:
        node = node.next
      new = Node(data)
      node.next = new
      new.prev = node # 새로운 노드의 prev에 직전 노드 주소 달아줌
      self.tail = new # 마지막노드를 new값으로 업데이트

  def desc(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next

# 노드 데이터가 특정 숫자인 노드 앞에 데이터를 추가하는 함수
  def insert_before(self,data,before_data):
    if self.head == None:
      self.head = Node(data)
      return True
    else:
      node = self.tail # 뒤에부터 검색
      while node.data != before_data:
        node = node.prev
        if node == None:
          return False # 앞에데이터가 없으니까 넣을 곳 없음
      temp = node.prev
      new = Node(data)
      if temp == None:
        self.head = new
        node.prev = new
        new.next = node
        return True
      else:
        temp.next = new 
        node.prev = new
        new.next = node
        new.prev = temp
        return True



double_linkedlist = NodeMgmt(0)
for data in range(1,10):
  double_linkedlist.insert(data)

double_linkedlist.insert_before(1.5,2)
double_linkedlist.desc()
