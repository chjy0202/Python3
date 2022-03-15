def possible(visit, col):
    current_row = len(visit)
    for row in range(current_row):
        if visit[row] == col or abs(visit[row] - col) == current_row - row:
            return False
    return True

# 파라미터 : n, 현재 행, 결과, 방문한 퀸의 행 번호가 담긴 리스트
def DFS(n, row, answer, visit):
    if row == n:
        answer += 1
        print(visit)
        print(answer)
        return answer

    # col : 현재 열
    for col in range(n):
        # 퀸을 이동할 수 없는 자리가 맞다면
        if possible(visit, col):
            visit.append(col)
            DFS(n, row + 1, answer, visit)
            # 이동할 수 없는 자리가 없을 때
            visit.pop()

def solution(n):
    answer = 0
    DFS(n, 0, answer, [])
    return answer