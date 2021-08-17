"나누어 떨어지는 숫자 배열"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12910"

def solution(arr, divisor):
    answer = []
    arr.sort()                                              # 배열 오름차순 정렬
    for i in range(len(arr)):                               # 배열의 요소를 탐색
        if arr[i] % divisor == 0 : answer.append(arr[i])    # 나누어 떠렁지는 경우, 리스트에 추가
    if len(answer) == 0 : answer.append(-1)                 # 리스트에 아무것도 없을 경우, -1을 추가
    return answer