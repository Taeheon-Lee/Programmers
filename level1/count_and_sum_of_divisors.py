"약수의 개수와 덧셈"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/77884"

def solution(left, right):
    answer = 0
    for i in range(left, right+1):  # 범위 탐색
        if i % (i**0.5) != 0:       # 제곱근이 존재하고 나누어 떨어지지 않을 경우, 개수는 반드시 짝수이기 때문에 덧셈
            answer += i
        else:                       # 떨어지는 경우, 개수는 반드시 홀수이기 때문에 뺄셈
            answer -= i
    return answer