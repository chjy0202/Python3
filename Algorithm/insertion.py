# 삽입정렬

# 맨앞의 데이터는 놔두고 다음데이터부터 앞의 데이터와 비교한다.
# 하나씩 뒤로가면서 앞의 데이터와 비교하는데 보다 작은 데이터가 나오면 그 앞에 삽입하고 그 턴은 끝난다.

import random

for idx in range(데이터길이 - 1):
  for idx2 in range(idx + 1, 0, -1):
    if 앞데이터 > 뒷데이터: 
      swap

def insertion_sort(data):
  for index in range(len(data) - 1):
    for index2 in range(index+1, 0, -1):
      if data[index2] < data[index2 - 1]:
        data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
      else: # 스왑이 일어나지 않으면 더이상 해당턴에서 비교 필요없음
        break
  return data


data_list = random.sample(range(100), 10)
print(insertion_sort(data_list))

# 시간복잡도 O(n^2)
