import random

def binary_search(data,search):
  if len(data) == 1 and search == data[0]:
    return True
  if len(data) == 1 and search != data[0]:
    return False
  if len(data) == 0:
    return False

  medium = len(data) // 2
  if search < data[medium]:
    return binary_search(data[:medium], search)
  elif search > data[medium]:
    return binary_search(data[medium:], search)
  elif search == data[medium]:
    return True
 

# data_list = random.sample(range(100),10)
data_list = [3,123,34,52,65,5,6,22]
data_list.sort()

print(data_list)
print(binary_search(data_list, 22))