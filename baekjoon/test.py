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
