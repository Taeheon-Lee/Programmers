"시저 암호"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12926"

def solution(s, n):                                                                     # 아스키코드 값을 이용하여 문자열 연산 수행
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        if s[i].islower() == True:
            s[i] = chr(ord(s[i]) + n if ord(s[i]) + n <= 122 else ord(s[i]) + n - 26)
        else:
            s[i] = chr(ord(s[i]) + n if ord(s[i]) + n <= 90 else ord(s[i]) + n - 26)
    answer = ''.join(s)
    return answer