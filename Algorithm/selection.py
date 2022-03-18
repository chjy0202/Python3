# 선택정렬

for stand in range(데이터길이 - 1):
	lowest = stand
	for idx in range(stand + 1, 데이터길이):
		if data[idx] < data[lowest]:
			lowest = idx
	swap(data[stand], data[lowest])

def selection_sort(data):
	for stand in range(len(data) - 1):
		lowest = stand # 맨 앞의 인덱스로 초기화
		for index in range(stand + 1, len(data)):
			if data[lowest] > data[index]:
				lowest = index
		# 한 번 턴을 돌면 최솟값의 인덱스가 lowest에 담겨있고 이를 맨 앞과 바꿔준다.
		data[lowest], data[stand] = data[stand], data[lowest]
	return data

import random

data_list = random.sample(range(100),10)
print(selection_sort(data_list))

# 시간복잡도 O(n^2)

