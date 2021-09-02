# 시간복잡도: 알고리즘 실행 속도
# 공간복잡도: 알 고리즘이 사용하는 메모리 사이즈
# 가장 핵심이 되는 것은 반 복 문!

def sum_all(n):
    total = 0
    for num in range(1, n+1):
        total += num
    return total
# 시간복잡도 : O(n)

def sum_all(n):
    return int(n*(n+1) / 2)
# 시간복잡도 : O(1) 더 효율적

print(sum_all(100))

