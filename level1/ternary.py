"3진법"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3"

def solution(n):
    rev_dec_to_tri = []                             # 3진법 변환 수를 뒤집어 저장할 리스트 생성
    while n != 0:
        rev_dec_to_tri.append(str(n%3))             # 3진법 나머지를 뒤에서부터 추가
        n //= 3
    answer = 0                                      # 정답 초기화
    tmp = 1
    while len(rev_dec_to_tri) != 0:
        answer += int(rev_dec_to_tri.pop(-1)) * tmp # 3진법수를 다시 10진법으로 초기화
        tmp *= 3
    return answer