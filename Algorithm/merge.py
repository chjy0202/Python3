def split(data):
	medium = len(data) // 2
	left = data[:medium]
	right = data[medium:]
	print(left,right)

data_list = [3,4,1,3,2]
# split(data_list)

def merge_split(data):
	if len(data) <= 1:
		return data
	medium = len(data) // 2
	left = merge_split(data[:medium])
	right = merge_split(data[medium:])
	# print(left,right)
	return merge(left, right)

data_list = [3,4,1,3,2,6,7,8]
merge_split(data_list)

 
  