# 퀵 정렬 - 정렬알고리즘의 꽃

# pivot을 정해서 그보다 작으면 왼 크면 오
# 재귀함수 사용

import random

def qsort(data):
  if len(data) <= 1:
    return data
  
  left, right = [], []
  pivot = data[0]

  for i in range(1,len(data)):
    # pivot 보다 작으면 왼쪽 리스트에 추가
    if pivot > data[i]:
      left.append(data[i])
    # pivot 보다 크면 오른쪽 리스트에 추가
    else:
      right.append(data[i])
  # 리스트끼리는 + 하기위해 [pivot] 으로 형변환
  return qsort(left) + [pivot] + qsort(right)

# data_list = random.sample(range(100),10)
# print(qsort(data_list))

# list comprehension
def qsort(data):
  if len(data) <= 1:
    return data
  
  pivot = data[0]

  left = [item for item in data[1:] if pivot > item]
  right = [item for item in data[1:] if pivot <= item]

  return qsort(left) + [pivot] + qsort(right)

data_list = random.sample(range(100),10)
print(qsort(data_list))
