string = '24431'

data = []
for i in string:
    data.append(int(i))

data.sort()
data = list(reversed(data)) # 리 스 트 변경 무조건
print(data)
# print(''.join(data)) int값은 안됨
for i in data:
    print(i,end='')