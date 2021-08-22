"타겟 넘버"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/43165"

def count(numbers, target, tmp, total):
    if tmp == len(numbers):                                     # 깊이 우선 탐색 사용, 마지막까지 이동했을 때,
        if total == target:                                     # 결과 값이 타겟 넘버와 동일할 경우, 1개를 추가하기 위해 1 리턴
            return 1
        return 0
    answer = 0                                                  # 타겟 넘버와 매칭되는 개수 초기화
    answer += count(numbers, target, tmp+1, total+numbers[tmp]) # 매칭되는 것을 더해줌 (더하기 탐색)
    answer += count(numbers, target, tmp+1, total-numbers[tmp]) # 매칭되는 것을 더해줌 (빼기 탐색)
    return answer

def solution(numbers, target):
    answer = count(numbers, target, 0, 0)
    return answer