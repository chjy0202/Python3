# 최대값과 최소값을 빠르게 찾기 위해 고안된 완전이진트리 (왼쪽부터 채워나간다)

# 데이터를 삽입할 때는 왼쪽부터 차례차레 채워나간다
# 부모보다 큰 수가 들어와도 우선은 데이터를 넣고 위의 부모노드와 비교해 가며 swap한다. 이 과정을 반복한다.

# 데이터를 삭제할 때는 대부분 root node가 삭제된다
# 이때는 마지막에 추가된 node를 root로 올린다
# 그리고 이후에 아래 자식노드 중 더 큰 수와 swap한다. 이 과정을 반복한다.

# 부모노드의 인덱스 번호 = 자식노드의 인덱스 번호 // 2
# 왼쪽은 부모노드의 인덱스 번호 * 2
# 오른쪽은 인덱스 번호 * 2 + 1

class Heap:
  def __init__(self,data):
    self.heap_array = list()
    self.heap_array.append(None) # 처음인덱스를 0아니고 1로 하고 싶어서
    self.heap_array.append(data)

  def insert(self, data):
    