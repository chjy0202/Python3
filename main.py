# 최대값과 최소값을 빠르게 찾기 위해 고안된 완전이진트리 (왼쪽부터 채워나간다)
# O(logn)의 시간이 소요됨.

# 부모노드는 항상 자식노드보다 크거나 같다. (최대힙)=> 최대값은 루트노드.
# 왼쪽, 오른쪽 자식노드 중에 무엇이 큰 값인지 모름

# 이진탐색 트리는 탐색을 위한 트리, 힙은 최대/최솟값 검색을 위한 트리.

# 데이터를 삽입할 때는 왼쪽부터 차례차레 채워나간다
# 부모보다 큰 수가 들어와도 우선은 데이터를 넣고 위의 부모노드와 비교해 가며 swap한다. 이 과정을 반복한다.

# 데이터를 삭제할 때는 대부분 root node가 삭제된다
# 이때는 마지막에 추가된 node를 root로 올린다
# 그리고 이후에 아래 자식노드 중 더 큰 수와 swap한다. 이 과정을 반복한다.

# 부모노드의 인덱스 번호 = 자식노드의 인덱스 번호 // 2 (몫)
# 왼쪽은 부모노드의 인덱스 번호 * 2
# 오른쪽은 인덱스 번호 * 2 + 1

class Heap:
  def __init__(self, data):
    self.heap_array = list()
    self.heap_array.append(None)  # 편하게 처음인덱스를 0아니고 1로 하고 싶어서
    self.heap_array.append(data)

  def move_up(self, inserted_idx):
    # 부모보다 커서 바꿔야 하는지 판단하는 method.
    if inserted_idx <= 1:
      return False
    parent_idx = inserted_idx // 2
    if self.heap_array[parent_idx] < self.heap_array[inserted_idx]:
      return True
    else:
      return False

  def insert(self, data):
    if len(self.heap_array) == 0:
      self.heap_array.append(None)
      self.heap_array.append(data)
      return True

    self.heap_array.append(data)
    # 들어간 노드가 상위 부모 노드보다 값이 클때
    # 인덱스번호. 우리는 인덱스0은 none으로 두고 1부터 보고 있기 때문
    inserted_idx = len(self.heap_array) - 1

    while self.move_up(inserted_idx):
      parent_idx = inserted_idx // 2
      self.heap_array[parent_idx], self.heap_array[inserted_idx] = self.heap_array[inserted_idx], self.heap_array[parent_idx]
      inserted_idx = parent_idx  # 원래 노드가 부모 노드로 바꼈기 때문

    return True

  # 삭제하는 코드
  def move_down(self, popped_idx):
    left_child_popped_idx = popped_idx * 2
    right_child_popped_idx = popped_idx * 2 + 1
    # 양쪽 모두 데이터가 있는 경우, 왼쪽만 있는 경우, 둘 다 없는 경우
    # 둘다 없는 경우
    if left_child_popped_idx >= len(self.heap_array):
      return False
    # 왼쪽만 있는 경우
    elif right_child_popped_idx >= len(self.heap_array):
      if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
        return True
      else:
        return False
    # 모두 있는 경우
    else:
      if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
        if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
          return True
        else:
          return False
      else:
        if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
          return True
        else:
          return False

    # if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
    #   self.heap_array[left_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_popped_idx]
    #   popped_idx = left_child_popped_idx    
    # elif self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
    #   self.heap_array[right_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[right_child_popped_idx]
    #   popped_idx = right_child_popped_idx  
    # else:
    #   return False

  def pop(self):
    if len(self.heap_array) <= 1:
      return None

    returned_data = self.heap_array[1] # 0은 비워놓고 1번으로 루트를 저장했기 때문에
    self.heap_array[1] = self.heap_array[-1] # 마지막꺼 올려주기
    del self.heap_array[-1]
    popped_idx = 1

    while self.move_down(popped_idx): # 이 부분 효율적으로 고쳐보기
      left_child_popped_idx = popped_idx * 2
      right_child_popped_idx = popped_idx * 2 + 1

      # 왼쪽만 있는 경우
      if right_child_popped_idx >= len(self.heap_array):
        if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
          self.heap_array[left_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_popped_idx]
          popped_idx = left_child_popped_idx    

      # 모두 있는 경우
      else:
        if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
          if self.heap_array[left_child_popped_idx] > self.heap_array[popped_idx]:
            self.heap_array[left_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_popped_idx]
            popped_idx = left_child_popped_idx    
        else:
          if self.heap_array[right_child_popped_idx] > self.heap_array[popped_idx]:
            self.heap_array[right_child_popped_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[right_child_popped_idx]
            popped_idx = right_child_popped_idx  

    return returned_data

      
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.heap_array)

print(heap.pop())
print(heap.heap_array)
heap.pop()
print(heap.heap_array)
heap.pop()
print(heap.heap_array)

