"두개 뽑아서 더하기"

# 문제 링크

import itertools

def solution(numbers):
    answer = []
    lst = list(itertools.permutations(numbers, 2))  # 2개 선택 순열 리스트 생성
    for elem in lst:                                # 리스트 내부 탐색
        answer.append(sum(elem))                    # 각 요소들의 합을 정답 리스트에 추가
    answer = sorted(set(answer))                    # 중복을 제거하고 정렬
    return answer

# 한 줄 작성

def solution(numbers):
    return sorted(set(sum(elem) for elem in list(itertools.permutations(numbers, 2))))