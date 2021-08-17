"2016년"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3"

week = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6:"WED", 0:"THU"}

def solution(a, b):
    days = b                                                    # 날짜 수
    m = 1
    while m < a:                                                # 선택된 달 이전 달까지 탐색
        if (m % 2 != 0 and m <= 7) or (m % 2 == 0 and m > 7):   # 7월 이하이고 홀수인 달과 8월 이상이고 짝수인 달은 31일을 카운트
            days += 31
        else:                                                   # 나머지의 경우에서 윤달은 29일을 뺴고, 30일 카운트
            days += 29 if m == 2 else 30
        m += 1
    answer = week[days%7]                                       # 7일로 나누어 나머지로 요일을 판단
    return answer