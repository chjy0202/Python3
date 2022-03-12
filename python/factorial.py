def factorial(n):
  if n > 1:
    return n * factorial(n - 1)
  return n

print(factorial(0))

def solution(입력):
  if 입력 > 일정값:
    return solution(입력 - 1) # 입력보다 작은 값
  return 일정값 or 특정값 # 재귀호출 종료