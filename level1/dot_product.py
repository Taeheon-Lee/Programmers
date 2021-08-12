"내적"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/70128"

def solution(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])    # 각 인덱스끼리 곱셈 값들의 합