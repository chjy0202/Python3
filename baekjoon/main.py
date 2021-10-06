# 1874

n = int(input())

count = 1
stack = []
result = []

for i in range(1,n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit()

print('\n'.join(result))



# 1920 (시간초과 -> set 수정)
# 1
n = int(input())
n_data = list(map(int,input().split())) # 집합으로 하면 메모리 시간 절약

m = int(input())
m_data = list(map(int,input().split())) 

for i in m_data:
    if i not in n_data:
        print(0)
    else:
        print(1)


# 2
n = int(input())
n_data = set(map(int,input().split()))

m = int(input())
m_data = list(map(int,input().split()))

for i in m_data:
    if i not in n_data:
        print(0)
    else:
        print(1)
        


# 1966

case = int(input())

for _ in range(case):
    n,m = map(int,input().split())
    queue = list(map(int,input().split()))
    queue = [(i,idx) for idx,i in enumerate(queue)]
    
    count = 0
    while True:
        if queue[0][0] == max(queue, key = lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:
                queue.pop(0)
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))


# 2798
# 1
from itertools import combinations

n, m = map(int,input().split())
data = list(map(int,input().split()))

result = 0
combi = list(combinations(data, 3))
    
for i in range(len(combi)):
    if sum(combi[i]) <= m and sum(combi[i]) > result :
        result = sum(combi[i])
print(result)
    

# 2
from itertools import combinations

n, m = map(int,input().split())
data = list(map(int,input().split()))

result = 0
combi = list(combinations(data, 3))
    
for i in range(len(combi)):
    if sum(combi[i]) <= m:
        result = max(sum(combi[i]), result) # 한번에 맥스로 수정
print(result)


# 2920
# 1
data = list(map(int,input().split( )))

if data[0] == 1:
    for i in range(7):
        if data[i+1] - data[i] != 1:
            print('mixed')
            exit()
    print('ascending')
elif data[0] == 8:
    for i in range(7):
        if data[i+1] - data[i] != -1:
            print('mixed')
            exit()
    print('descending')
else:
    print('mixed')

# 2 훨씬 효율적
data = list(map(int,input().split()))

desc = True
asc = True

for i in range(7):
    if data[i+1] > data[i]:
        desc = False
    elif data[i+1] < data[i]:
        asc = False

if desc:
    print('descending')
elif asc:
    print('ascending')
else:
    print('mixed')



# 5397
# 1
case = int(input())

for _ in range(case):
    data = input()
    left_stack = []
    right_stack = []
    
    for i in data:
        if i == '-':
            if left_stack: # 값이 있다면
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))

    # result = left_stack + list(reversed(right_stack)) 
    # print(''.join(result))
    