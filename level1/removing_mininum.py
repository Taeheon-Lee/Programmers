"제일 작은 수 제거하기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12935"

def solution(arr):
    if len(arr) <= 1:       # 리스트의 길이가 1개 이하일 경우, [-1] 리스트 출력
        return [-1]
    arr.remove(min(arr))    # 길이가 2이상인 경우, 가장 작은 수를 제거하고 출력
    return arr