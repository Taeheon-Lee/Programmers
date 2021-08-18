"약수의 합"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12928"

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:      # 약수일 경우
            answer += i     # 더하기
    return answer