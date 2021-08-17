"두 정수 사이의 합"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3"

def solution(a, b):
    return sum([i for i in range(a if a < b else b, b+1 if a < b else a+1)])