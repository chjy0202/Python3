# 노트생성
class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None

# 이진탐색트리
class NodeMgmt:
  def __init__(self,head):
    self.head = head # 루트 노드

  def insert(self,value):
    self.current_node = self.head
    while True:
      if value < self.current_node.value:
        if self.current_node.left != None:
          self.current_node = self.current_node.left
        else:
          self.current_node.left = Node(value) # 왼쪽에 없으면 생성
          break
      else:
        if self.current_node.right != None:
          self.current_node = self.current_node.right
        else:
          self.current_node.right = Node(value) # 오른쪽에 없으면 생성
          break
    
  # 서치코드
  def search(self,value):
    self.current_node = self.head
    while self.current_node:
      if self.current_node.value == value:
        return True
      elif self.current_node.value > value:
        self.current_node = self.current_node.left
      else:
        self.current_node = self.current_node.right
    return False


head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(0)
BST.insert(6)
BST.insert(3)

# print(BST.search(6))

