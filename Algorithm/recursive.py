import random

def factorial(num):
  if num > 1:
    return num * factorial(num-1)
  else:
    return num

# for num in range(10):
  # print(factorial(num))


# 예제 1
def multiple(num):
  result = 1
  for i in range(1,num+1):
    result = result * i
  return result
# print(function(3))

def multiple_re(num):
  if num > 1:
    return num * multiple_re(num-1)
  else:
    return num
# print(multiple_re(4))



# 예제 2
data = random.sample(range(100),10)
# print(data)

def sum(data):
  result = 0
  for i in range(len(data)):
    result += data[i]
  print(result)
# print(sum(data))

def sum_re(data):
  if len(data) <= 1:
    return data[0]
  else:
    return data[0] + sum_re(data[1:])
# print(sum_re(data))



# 예제 3(회문)
def check(string):
  count = len(string) // 2
  for i in range(count):
    if string[i] != string[-1-i]:
      return False
  return True

# print(check('abba'))

def check_re(string):
  if len(string) <= 1:
    return True
  else:
    if string[0] == string[-1]:
      return check_re(string[1:-1])
    else:
      return False

# print(check_re('aba'))


# 예제 4
def function(num):
  print(num)
  if num <= 1:
    return num

  if num % 2 == 1:
    return function(3 * num +1)
  else:
    return function(num//2)

# function(3)


# 예제 5
def sum_count(n):
  if n <= 1:
    return 1
  elif n == 2:
    return 2
  else:
    return sum_count(n-1) + sum_count(n-2) + sum_count(n-3)
print(sum_count(6))