# 순차탐색
from random import *

rand_data_list = list()
for num in range(10):
	rand_data_list.append(randint(1,100))

def sequencial(data,search):
	for i in range(len(data)):
		if data[i] == search:
			return i
	return -1
