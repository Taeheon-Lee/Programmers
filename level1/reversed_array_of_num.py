"자연수 뒤집어 배열로 만들기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12932"

def solution(n):
    return list(map(int, reversed(str(n)))) # 정루를 문자열화 시켜 뒤집어 리스트로 만든 뒤, 각 요소를 다시 정수로 변환