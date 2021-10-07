# 동적계힉법(dynamic) 과 분할정복(divide)
# 공통점 -  입력크기가 작은 문제들을 해결 한 후, 해당 문제의 해를 활용해서 보다 큰 부분 문제를 해결

# 차이점
# 동적 - Memorization 기법을 사용해서 저장. 
# 동적 - 상향식 접근법
# 피보나치 수열 

# 분할 - 하양식 접근법. 일반적으로 재귀함수로 구현.
# 분할 - 부분문제가 서로 중복되지 않는다.

# 피보를 recursive로 만들고 이를 보완하는 다이나믹으로 수정해 보기
def fibo(num):
	if num <=1 :
		return num
	return fibo(num-1) + fibo(num-2)

# print(fibo(4))

def fibo_dp(num):
	cache = [0 for i in range(num+1)]
	cache[0] = 0
	cache[1] = 1

	for index in range(2, num+1):
		cache[index] = cache[index-1] + cache[index-2]
	return cache[num]

print(fibo_dp(10))