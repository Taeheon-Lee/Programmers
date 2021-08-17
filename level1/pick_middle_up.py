"가운데 글자 가져오기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3"

def solution(s):
    answer = s[len(s)//2] if len(s)%2 != 0 else s[len(s)//2-1:len(s)//2+1]  # 중간 글자를 가져오되, 홀수 길이일 경우, 한개, 짝수 길이인 경우, 두개를 가져옴
    return answer