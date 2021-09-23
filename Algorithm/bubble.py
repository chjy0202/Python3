# 버블정렬

def bubblesort(data):
  for index in range(len(data) - 1):
    swap = False
    for index2 in range(len(data) - index - 1):
      if data[index2] > data[index2 + 1]:
        data[index2], data[index2 + 1] = data[index2 + 1],data[index2]
        swap = True # 턴이 실행이 될 때 마다 true로 바뀐다. 
    if swap == False:
      break
  return data


import random
data_list = random.sample(range(100), 50)
# print(data_list)
print(bubblesort(data_list))

# 시간복잡도 O(n^2)