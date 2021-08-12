"크레인 인형 뽑기 게임"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/64061"

def solution(board, moves):
    answer = 0
    stack = []                                                      # 스택 생성
    for loc in moves:
        loc -= 1                                                    # 배열 인덱스는 0부터 시작하기 때문에 -1
        for i in range(len(board)):                                 # 인형 뽑기 기계를 선택된 위치에서 아래로 탐색
            if board[i][loc] != 0:                                  # 해당 라인에 인형이 존재할 경우, 인형을 선택
                if len(stack) == 0 or stack[-1] != board[i][loc]:   # 스택에 아무것도 없거나, 스택에 있는 마지막 인형이 선택된 인형과 다를 경우
                    stack.append(board[i][loc])                     # 스택에 인형을 추가
                else:                                               # 같을 경우
                    stack.pop(-1)                                   # 스택에 있는 마지막 인형과, 선택한 인형을 터트리고 터트린 인형 수 2개 카운트
                    answer += 2
                board[i][loc] = 0                                   # 기계에 선택된 라인에 있는 인형을 뽑았기 때문에 해당 인형을 없앰
                break                                               # 인형이 탐색된 경우 더 이상 탐색하지 않고 반복문을 빠져나감
    return answer