"콜라츠 추측"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12943"

def solution(num):
    answer = 0
    while (num != 1):
        if answer > 500:                                # 500번 넘게 반복해도 나오지 않으면 -1 출력
            return -1
        num = num // 2 if num % 2 == 0 else num * 3 + 1 # 짝수면 2로 나누고, 홀수면 3을 곱하고 1을 더하는 작업 반복
        answer += 1
    return answer