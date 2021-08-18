"이상한 문자 만들기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12930"

def solution(s):
    s = list(s)                                                     # 문자를 하나씩 치환하여 넣기 위해서는 문자열에서 처리가 불가능하고 리스트화 시켜 처리
    check = 0                                                       # 문자 위치 변수 초기화
    for i in range(len(s)):
        if s[i] == ' ':                                             # 단어가 끝난 경우, 문자 위치를 다시 0으로 초기화
            check = 0
        else:
            s[i] = s[i].upper() if check % 2 == 0 else s[i].lower() # 단어의 문자가 홀수 번쨰면 소문자, 짝수 번쨰면 대문자로 변환 
            check += 1                                              # 문자 위치를 넘김
    answer = ''.join(s)                                             # 리스트를 다시 문자열로 변환
    return answer