# 버블정렬

for index in range(데이터길이 - 1):
  for index2 in range(데이터길이 - index - 1):
    if 앞데이터 > 뒷데이터:
      swap(앞데이터, 뒷데이터)

def bubblesort(data):
  for index in range(len(data) - 1):
    swap = False
    for index2 in range(len(data) - index - 1):
      if data[index2] > data[index2 + 1]:
        data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
        swap = True # 턴이 실행이 될 때 마다 true로 바뀐다. 
    if swap == False:
      break # 스왑이 일어나지 않았으니 이미 정렬이 완료된 상태
  return data


import random
data_list = random.sample(range(100), 50)
# print(data_list)
print(bubblesort(data_list))

# 시간복잡도 O(n^2)