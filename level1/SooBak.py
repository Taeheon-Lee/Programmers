"수박수박수박수박수박수?"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12922"

def solution(n):
    answer = "수박" * (n // 2) # 문자열 반복을 연산자를 이용하여 반복
    if n % 2 != 0:
        answer += "수"
    return answer