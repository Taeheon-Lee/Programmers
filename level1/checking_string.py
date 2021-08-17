"문자열 다루기 기본"

# 문자 링크 "https://programmers.co.kr/learn/courses/30/lessons/12918"

def solution(s):
    if s.isdigit():                     # 문자열이 숫자로 이우어져 있는지 비교
        if len(s) == 4 or len(s) == 6:  # 숫자로 이루어져 있는 경우, 길이가 4 또는 6 인지 확인
            return True
    return False