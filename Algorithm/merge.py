import random


def split(data):
	medium = len(data) // 2
	left = data[:medium]
	right = data[medium:]
	print(left, right)


# data_list = [3, 4, 1, 3, 2]
# split(data_list)


def merge_split(data):
	if len(data) <= 1:
		return data
	medium = len(data) // 2
	left = merge_split(data[:medium])
	right = merge_split(data[medium:])
	# print(left, right)
	return merge(left, right)


# data_list = [3, 4, 1, 3, 2, 6, 7, 8]
# merge_split(data_list)

def merge(left, right):
	merged = list()
	lp, rp = 0, 0

	while len(left) > lp and len(right) > rp:
		if left[lp] > right[rp]:
			merged.append(right[rp])
			rp += 1
		else:
			merged.append(left[lp])
			lp += 1

	while len(left) > lp:
		merged.append(left[lp])
		lp += 1
	while len(right) > rp:
		merged.append(right[rp])
		rp += 1

	# print(merged)
	return merged

data_list = random.sample(range(100),10)
# print(data_list)

print(merge_split(data_list))

