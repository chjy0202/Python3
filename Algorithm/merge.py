import random

# 리스트를 자르는 함수
def split(data):
	medium = len(data) // 2
	left = data[:medium]
	right = data[medium:]
	print(left, right)


# data_list = [3, 4, 1, 3, 2]
# split(data_list)


def merge_split(data):
	# 데이터 길이가 1일때 까지 재귀적으로 함수를 계속 불러온다.
	if len(data) <= 1:
		return data
	medium = len(data) // 2
	left = merge_split(data[:medium])
	right = merge_split(data[medium:])
	return merge(left, right)


# data_list = [3, 4, 1, 3, 2, 6, 7, 8]
# merge_split(data_list)

def merge(left, right):
	merged = list()
	lp, rp = 0, 0

	# case1 : left, right 가 아직 남아있을 때
	while len(left) > lp and len(right) > rp:
		if left[lp] > right[rp]:
			merged.append(right[rp])
			rp += 1
		else:
			merged.append(left[lp])
			lp += 1

	# case2 : left 만 남아있을 때
	while len(left) > lp:
		merged.append(left[lp])
		lp += 1

	# case3 : right 만 남아 있을 때 
	while len(right) > rp:
		merged.append(right[rp])
		rp += 1

	return merged

data_list = random.sample(range(100),10)
# print(data_list)

print(merge_split(data_list))

# 시간복잡도 O(n logn)