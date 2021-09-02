hash_table = list([0 for i in range(10)])
# print(hash_table) 

# division 법
def hash_func(key):
  return key % 5

data1 = 'Andy'
data2 = 'Dave'
data3 = 'trump'

# print(ord(data1[0]), hash_func(ord(data2[0])))

def storage_data(data,value):
  key = ord(data[0])
  hash_address = hash_func(key)
  hash_table[hash_address] = value

storage_data('Andy', '01055553333')
storage_data('Dave', '01044443333')
storage_data('Trump', '01022223333')

def get_data(data):
  key = ord(data[0])
  hash_address = hash_func(key)
  print(hash_table[hash_address])

get_data('Andy')


# 주소가 동일 할 경우 충돌을 해결하기 위한 별도 자료구조가 필요함

hash_table = list([0 for i in range(8)])

def get_key(data):
  return hash(data)

def hash_function(key):
  return key % 8

def save_data(data,value):
  hash_address = hash_function(get_key(data))
  hash_table[hash_address] = value

def read_data(data):
  hash_address = hash_function(get_key(data))
  return hash_table[hash_address]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
read_data('Dave')

print(hash_table) 






# 충돌이 생길때

hash_table = list([0 for i in range(8)])

def get_key(data):
  return hash(data)

def hash_function(key):
  return key % 8

def save_data(data,value):
  # 충돌 생길때
  index_key = get_key(data)

  hash_address = hash_function(index_key)
  if hash_table[hash_address] != 0:
  # 0이 아니면 값이 들어있다는 얘기
    for index in range(len(hash_table[hash_address])):
      if hash_table[hash_address][index][0] == index_key:
        hash_table[hash_address][index][1] = value
        return
    hash_table[hash_address].append([index_key, value])
  else:
    hash_table[hash_address] = [[index_key, value]]
      

def read_data(data):
  index_key = get_key(data)
  hash_address = hash_function(index_key)
  if hash_table[hash_address] != 0:
    for index in range(len(hash_table[hash_address])):
      if hash_table[hash_address][index][0] == index_key:
        return hash_table[hash_address][index][1]
    return None
  else:
    return None
     

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
read_data('Dave')

print(hash_table)

 