"정수 제곱근 판별"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12934"

def solution(n):
    return (n**0.5+1)**2 if (n**0.5).is_integer() else -1 # 입력 값이 정수 제곱근이 존재할 경우, 제곱근+1 제곱 값 출력, 아닐 경우, -1