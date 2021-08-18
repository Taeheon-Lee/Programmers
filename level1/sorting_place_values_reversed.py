"정수 내림차순으로 배치하기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12933"

def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True))) # 정수를 문자열 리스트화 시킨 뒤, 내림차순 정렬하여 다시 문자열화 한 후 정수화