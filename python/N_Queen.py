def possible(visit, col):
    current_row = len(visit)
    for row in range(current_row):
        if visit[row] == col or abs(visit[row] - col) == current_row - row:
            return False
    return True

# 파라미터 : n, 현재 행, 방문한 퀸의 행 번호가 담긴 리스트
def DFS(n, row, visit):
    answer = 0
    if row == n:
        return 1
    
    # col : 현재 열
    for col in range(n):
        # 퀸을 이동할 수 없는 자리가 맞다면
        if possible(visit, col):
            visit.append(col)
            answer += DFS(n, row + 1, visit)
            # 이동할 수 없는 자리가 없을 때
            visit.pop()
    return answer

def solution(n):
    return DFS(n, 0, [])