"휴대폰 번호 가리기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12948"

def solution(phone_number):
    return "*" * (len(phone_number)-4) + phone_number[-4:]