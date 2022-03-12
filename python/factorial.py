def factorial(n):
  if n > 1:
    return n * factorial(n - 1)
  return n

print(factorial(0))

def solution_(입력):
  if 입력 > 일정값:
    return solution(입력 - 1) # 입력보다 작은 값
  return 일정값 or 특정값 # 재귀호출 종료

# 회문(거꾸로 읽어도 제대로 읽은 것과 동일한 단어나 문장)
def solution(s):
  if len(s) <= 1:
    return True
  if s[0] == s[-1]:
    return solution(s[1: -1])
  return False

# print(solution('level'))
    