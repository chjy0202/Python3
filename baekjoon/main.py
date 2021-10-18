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
    

# 4195 다시풀어보기

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x
        number[x] += number[y]
    

case = int(input())

for _ in range(case):
    parent = dict()
    number = dict() #네트워크
    
    f = int(input())
    
    for _ in range(f):
        x,y = input().split()
        
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
            
        union(x,y)
        print(number[find(x)])


# 2750 정렬

n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))
for i in sorted(data):
    print(i)

# 1427
# 1
data = input()

for i in range(9,-1,-1):
    for j in data:
        if int(j) == i:
            print(i, end='')

# 2
string = input()

data = []
for i in string: # 문자열 스트링 반복문으로 한문자씩 가져오기
    data.append(int(i))

data.sort()
data = list(reversed(data)) # 리 스 트 변경 무조건

# print(''.join(data)) int형은 join 안됨?

for i in data:
    print(i,end='')


# 10814
case = int(input())

data = []
for _ in range(case):
    input_data = input().split()
    data.append((int(input_data[0]),input_data[1])) # 다시 튜플형으로. 숫자는 인트형으로. 
    
data.sort(key = lambda x : x[0])

for i in data:
    print(i[0], i[1])


# 11650
# 1
case = int(input())

data = []
for _ in range(case):
    input_data = input().split()
    data.append((int(input_data[0]),int(input_data[1]))) # int로 제발 바꿔야 함!!
    
data.sort(key = lambda x: (x[0],x[1])) # 첫번째 값으로 정렬하고 똑같으면 2번쨰로 정렬하는 법

for i in data:
    print(i[0], i[1])

# 2
# 근데 파이썬은 사실 기본정렬이 "첫번째 값으로 정렬하고 똑같으면 2번쨰로 정렬하는 법" 이게 디폴트임
# 그래서 key 없이 가능

case = int(input())

data = []
for _ in range(case):
    x,y = map(int,input().split()) 
    data.append((x,y))

data.sort()

for i in data:
    print(i[0], i[1])



# 10989

# 계수정렬
# case수는 많고(10,000,000 이상) 수의범위는 제한이 될 때 사용하는 알고리즘
# 배열의 인덱스를 데이터의 값으로 여긴다. 미리 크기를 선언해야 한다.
# 데이터가 등장하는 횟수를 카운트 하는것
# 인덱스의 값만큼 그 인덱스 숫자를 반복 출력한다

# python 에서는 데이터의 갯수가 많을 때 sys.stdin.readline() 을 input()대신 사용한다.

import sys

case = int(sys.stdin.readline())
array = [0] * 10001

for _ in range(case):
    data = int(sys.stdin.readline())
    array[data] += 1
    
for idx in range(10001):
    if array[idx] != 0:
        for _ in range(array[idx]):
            print(idx)



# 2747
# 재귀용법

# 1 시간초과 생김
num = int(input())

def fibo(n):
    if n == 0 or n == 1:
        return n
    elif n >= 2:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(num))

# 2 반복문

num = int(input())

a,b = 0,1

while num > 0:
    a,b = b, a+b
    num -= 1
    
print(a)

# 3 memorization

num = int(input())

def fibo(num):
    cache = [0 for _ in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for idx in range(2,num+1):
        cache[idx] = cache[idx-1] + cache[idx-2]
    return cache[num]

print(fibo(num))


# 1074 다시보기

def solve(n,x,y):
    global result
    if n == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y+1 == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y == Y:
            print(result)
            return
        result += 1
        if x+1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return
    
    solve(n/2, x, y)
    solve(n/2, x, y+n/2)
    solve(n/2, x+n/2, y)
    solve(n/2, x+n/2, y+n/2)
    
result = 0
N, X, Y = map(int, input().split())
solve(2 ** N, 0, 0)


# 7490

# 1543
# 1
data = input()
check = input()

i, count = 0,0

while i < len(data):
    if data[i:i+len(check)] == check:
        count += 1
        i += len(check)
        continue
    i += 1
print(count)

# 2
data = input()
check = input()

i, count = 0,0

while len(data) - i >= len(check):
    if data[i:i+len(check)] == check: # 남은문자가 check문자의 길이보다 같거나 클때
        count += 1
        i += len(check)
    else:
        i += 1
print(count)


# 1568
n = int(input())

i, min = 1,0
while n > 0:
    if n >= i:
        n -= i
        i += 1
        min += 1
    else:
        i = 1
print(min)



# 1302 딕셔너리를 이용한 탐색
num = int(input())

data = dict()
for _ in range(num):
    title = input()
    if title not in data:
        data[title] = 1
    else:
        data[title] += 1
        
# data.sort(reverse = True, key = lambda x: x.values)
max_value = max(data.values())
li = []

for k,v in data.items():
    if v == max_value:
        li.append(k)
li.sort()
print(li[0])



# 1668
# 1
num = int(input())

data = []
for _ in range(num):
    data.append(int(input()))
    
left_count = 1
right_count = 1

left_value = data[0]
right_value = data[-1]


for i in range(1,len(data)):
    if data[i] > left_value:
        left_count += 1
        left_value = data[i]

for j in range(len(data)-2,-1,-1):
    if data[j] > right_value:
        right_count += 1
        right_value = data[j]

print(left_count, right_count, sep = '\n')



# 1236
n, m = map(int,input().split())
arr = []

for _ in range(n):
    arr.append(input())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            row[i] = 1
            column[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

column_count = 0
for j in range(m):
    if column[j] == 0:
        column_count += 1

print(max(row_count,column_count))


# 1260
from collections import deque

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if visited[e] == False:
            dfs(e)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if visited[v] == False:
            print(v,end = ' ')
            visited[v] = True
            for e in adj[v]:
                if visited[e] == False:
                    q.append(e)
            


n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

for e in adj:
    e.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)