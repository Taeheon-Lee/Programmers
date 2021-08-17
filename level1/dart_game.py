"다트 게임"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/17682"

bonus = {"S":1,"D":2,"T":3}

def solution(dartResult):
    stack = []
    for i in range(len(dartResult)):                                        # dart 결과를 1개씩 탐색
        if dartResult[i].isdigit():                                         # 결과가 숫자일 경우
            if dartResult[i] == "0" and i != 0 and dartResult[i-1] == "1":  # 10점인지 확인
                stack[-1] = 10
            else:                                                           # 아닐 경우, 숫자를 스택에 삽입
                stack.append(int(dartResult[i]))
        elif dartResult[i] in ["S","D","T"]:                                # 결과가 영역일 경우
            stack[-1] **= bonus[dartResult[i]]                              # 보너스 계산
        elif dartResult[i] == "*":                                          # 스타상일 경우
            stack[-1] *= 2
            if len(stack) >= 2:                                             # 점수가 제일 첫 점수가 아닐 경우
                stack[-2] *= 2
        else:                                                               # 아차상일 경우
            stack[-1] *= -1
    answer = sum(stack)                                                     # 결과를 합산
    return answer