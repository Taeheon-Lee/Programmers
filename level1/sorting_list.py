"문자열 내 마음대로 정렬하기"

# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = sorted(strings, key = lambda x : (x[n], x)) # x 리스트의 n번 인덱스 기준으로 정렬 뒤, 같을 경우, 문자순으로 정렬
    return answer