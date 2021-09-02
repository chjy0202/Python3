# 노트생성
from typing import ChainMap


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


# 이진탐색트리 삭제 
# leaf Node삭제
# child Node가 하나일때 (branch가 1개 일때)
# branch가 2개 일때 
# - 삭제할 node의 오른쪽 자식 중, 가장 작은 값을 삭제할 node의 parant Node가 가리키도록 한다.
# 1. 삭제할 node의 오른쪽 자식 선택
# 2. 오른쪽 자식의 가장 왼쪽에 있는 node 선택
# 3. 해당 node를 삭제할 node의 parent node 의 오른쪽/왼쪽 branch가 가리키게 함
# 4. 해당 node의 왼쪽 branch가 삭제할 node의 왼쪽 child node를 가리키게 함
# 5. 해당 node의 오른쪽 branch가 삭제할 node의 오른쪽 child node를 가리키게 함
# 6. 만약 해당 node가 오른 쪽 child node를 가지고 있었을 경우에는 , 해당 node의 본래 parent node의 왼쪽 branch로 연결
# - ( 삭제할 노드의 왼쪽 자식 중, 가장 큰 값을 올린다. )


  # 삭제코드
  def delete(self,value):
    searched = False
    self.current_node = self.head
    self.parent = self.head
    while self.current_node:
      if self.current_node.value == value:
        searched = True
        break
      elif self.current_node.value > value:
        self.parent = self.current_node
        self.current_node = self.current_node.left
      else:
        self.parent = self.current_node
        self.current_node = self.current_node.right
    if searched == False:
      return False
    
    # 이후부터 케이스를 분리해서 코드 작성

    # 리프노드일때
    if self.current_node.left == None and self.current_node.right == None:
      if value < self.parent.value:
        self.parent.left = None
      else:
        self.parent.right = None
      del self.current_node
    # branch가 1개 일때
    elif self.current_node.left != None and self.current_node.right == None:
      if value < self.parent.value:
        self.parent.left = self.current_node.left
      else:
        self.parent.right = self.current_node.left
    elif self.current_node.left == None and self.current_node.right != None:
      if value < self.parent.value:
        self.parent.left = self.current_node.right
      else:
        self.parent.right = self.current_node.right
    # 브렌치가 2개 일때 (삭제할 노드가 parent 의 왼쪽에 있는지 오른쪽에 있는지 나눠서)
    # 왼쪽에 있을 때
    elif self.current_node.left != None and self.current_node.right != None:
      if value < self.parent.value:
        self.change_node = self.current_node.right
        self.change_node_parent = self.current_node.right
        while self.change_node.left:
          self.change_node_parent = self.change_node
          self.change_node = self.change_node.left
        if self.change_node.right != None:
          self.change_node_parent.left = self.change_node.right
        else:
          self.change_node_parent.left = None
        self.parent.left = self.change_node
        self.change_node.left = self.current_node.left
        self.change_node.right = self.current_node.right
      # 오른쪽에 있을 때
      else:
        self.change_node = self.current_node.right
        self.change_node_parent = self.current_node.right
        while self.change_node.left:
          self.change_node_parent = self.change_node
          self.change_node = self.change_node.left
        if self.change_node.right != None:
          self.change_node_parent.left = self.change_node.right
        else:
          self.change_node_parent.left = None
        self.parent.right = self.change_node
        self.change_node.left = self.current_node.left
        self.change_node.right = self.current_node.right
    
    return True

head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(0)
BST.insert(6)
BST.insert(3)

BST.search(6)

# 1-1000 숫자 중에서 임의로 100개를 추출해서 이진 탐색 트리에 입력, 검색, 삭제
import random

bst_nums = set() # 집합(중복없음)
while len(bst_nums) != 100:
  bst_nums.add(random.randint(0,999))

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 한다. 
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
  binary_tree.insert(num)

# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
  if binary_tree.search(num) == False:
    print('search failed',num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
  delete_nums.add(bst_nums[random.randint(0,99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
  if binary_tree.delete(del_num) == False:
    print('delete failed', del_num)