"문자열 내 p와 y의 개수"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12916"

def solution(s):
    s = s.lower()                       # 문자열을 모두 소문자로 변경
    if s.count('p') != s.count('y'):    # count 함수를 이용하여 비교
        return False
    return True