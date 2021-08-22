"자릿수 더하기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12931"

def solution(n):
    return sum(map(int, list(str(n))))  # 숫자를 각 문자열 리스트화 시킨 뒤 정수화 시켜 합을 구함