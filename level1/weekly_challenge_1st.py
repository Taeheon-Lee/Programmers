"위클리 챌린지 1주차"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/82612"

def solution(price, money, count):
    total_cost = (count * (price + price * count)) / 2      # 등차 수열의 합 공식 사용 (초항 price, 공차 price, 항수 n)
    return total_cost - money if total_cost > money else 0  # 조건에 따라 출력