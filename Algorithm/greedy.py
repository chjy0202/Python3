# 탐욕 알고리즘 = 그리디
# 매순간 최적이라고 생각되는 경우를 선택하는 방식
# 최적의 해라고 확정할 수는 없지만 최적의 해에 가까운 값을 구하기 위해 사용됨

# 동전 문제
coin_list = [500.,100,50,1]

def min_coin_count(value,coin_list):
	total_coin_count = 0
	details = []
	coin_list.sort(reverse = True)

	for coin in coin_list:
		coin_num = value // coin
		total_coin_count += coin_num
		value -= coin_num * coin
		details.append([coin,coin_num])
	return total_coin_count


# 몫 나머지 방법
def solution(value, coin_list):
	total_coin_count = 0
	coin_list.sort(reverse = True) # 큰 순서로 정렬

	for i in range(len(coin_list)):
		re = divmod(value,coin_list[i])
		total_coin_count += int(re[0])
		value = re[1]
	
	return total_coin_count

print(min_coin_count(4720, coin_list))
print(solution(4720, coin_list))

# 부분 배낭 문제
