"문자열 내림차순으로 배치하기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12917"

def solution(s):
    answer = ''.join(sorted(s, reverse=1)) # 문자열을 내림차순으로 정렬 리스트화 시키고 join() 함수로 합침
    return answer