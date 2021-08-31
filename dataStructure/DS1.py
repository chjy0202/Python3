#배열

dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

cnt = 0
for i  in dataset:
  for j in i:
    if j == 'M':
      cnt += 1
print(cnt)




# 큐

import queue

data_q = queue.Queue()

data_q.put("conding")
data_q.put(56)

print(data_q.qsize())
print(data_q)
print(data_q.get())
print(data_q.get())
print(data_q.qsize())



data_lifoq = queue.LifoQueue()

data_lifoq.put("aaaa")
data_lifoq.put(22)

print(data_lifoq.get())

 
data_pq = queue.PriorityQueue()

data_pq.put((10,"korea"))
data_pq.put((5,25))
data_pq.put((7,"pizza"))

print(data_pq.qsize())
print(data_pq.get())
print(data_pq.get())

queue_list = list()

def enqueue(data):
  queue_list.append(data)

def dequeue():
  queue_list.remove(queue_list[0])

enqueue('2')
enqueue("pixxa")
dequeue()
print(queue_list)
dequeue()
print(queue_list)




#스택

def recursive(data):
  if data<0:
    print('ended')
  else:
    print(data)
    recursive(data-1)
    print('returned',data)

recursive(4)


data_stack = list()
data_stack.append(1)
data_stack.append(2)

print(data_stack)
print(data_stack.pop())
print(data_stack.pop())
print(data_stack)

stack_list = list()

def push(data):
  stack_list.append(data)
  print(stack_list)
def pop():
  stack_list.remove(stack_list[-1])
  del stack_list[-1]
  print(stack_list)

push(3)
push(7)
push(56)
pop()

