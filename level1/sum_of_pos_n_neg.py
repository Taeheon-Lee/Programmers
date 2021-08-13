"음양 더하기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/76501"

def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else -1*absolutes[i] for i in range(len(absolutes))]) # 조건식과 반복문을 한 줄에 작성하여 sum함수를 이용하여 리턴