"행렬 테두리 회전하기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/77485"

def solution(rows, columns, queries):
    answer = []
    frame = [[i for i in range(j*columns+1, (j+1)*columns+1)] for j in range(rows)] # 행렬 생성
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1                                     # 인덱스는 0부터 시작하기 때문에 각 위치를 모두 -1
        h = x2 - x1                                                                 # 가로 길이
        v = y2 - y1                                                                 # 세로 길이
        min_num = frame[x1][y1]                                                     # 이동한 값 중 가장 작은 값을 frame[x1][y1] 값으로 초기화
                                                                                    # 시계 방향으로 이동하기 위하여, 이동 전 값을 다음 값으로 넣기 위해 시계 반대 방향으로 변환
        tmp = frame[x1][y1]                                                         # 이때, 시계 반대 방향으로 돌면 시작 값이 사라지는 현상이 발생하여 tmp로 미리 저장
        for i in range(x1, x1+h):                                                   # 회전 변환 시작
            frame[i][y1] = frame[i+1][y1]
            if frame[i+1][y1] < min_num:                                            # 변환 중 이동 값이 저장한 가장 작은 값보다 작은 경우 이 값을 가장 작은 값으로 선택
                min_num = frame[i+1][y1]
        for i in range(y1, y1+v):
            frame[x2][i] = frame[x2][i+1]
            if frame[x2][i+1] < min_num:                                            # 변환 중 이동 값이 저장한 가장 작은 값보다 작은 경우 이 값을 가장 작은 값으로 선택
                min_num = frame[x2][i+1]
        for i in range(x2, x2-h, -1):
            frame[i][y2] = frame[i-1][y2]
            if frame[i-1][y2] < min_num:                                            # 변환 중 이동 값이 저장한 가장 작은 값보다 작은 경우 이 값을 가장 작은 값으로 선택
                min_num = frame[i-1][y2]
        for i in range(y2, y2-v, -1):
            frame[x1][i] = frame[x1][i-1]
            if frame[x1][i-1] < min_num:                                            # 변환 중 이동 값이 저장한 가장 작은 값보다 작은 경우 이 값을 가장 작은 값으로 선택
                min_num = frame[x1][i-1]
        frame[x1][y1+1] = tmp                                                       # 마지막 변환 값을 시작 값으로 바꾸어야 하는데 최초 변환에 의하여 사라졌기 때문에 따로 저장한 tmp 값으로 변환
        answer.append(min_num)                                                      # 이동한 값 중 가장 작은 값 answer 리스트에 추가
    return answer