"같은 숫자는 싫어"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12906"

def solution(arr):
    answer = []
    tmp = -1                    # 비교 변수 초기화
    for elem in arr:
        if tmp != elem:         # 기존 변수와 달라질 경우
            answer.append(elem) # 리턴 리스트에 추가
            tmp = elem          # 비교 변수를 바뀐 변수로 변경
    return answer