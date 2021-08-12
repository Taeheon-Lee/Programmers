"체육복 (Personal Education Clothes)"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/42862"

def solution(n, lost, reserve):
    real_lost = []                      # for문 반복 시, remove 사용하여 탐색 중 가운데를 삭제될 경우, 삭제된 것을 고려하지 않고 다음으로 가기 때문에 한 칸을 더 넘어가게 됨
                                        # 따라서 진짜 체육복이 없는 사람을 포함할 새로운 리스트 생성
    for person in lost:
        if person in reserve:           # 도난 당했으나, 여벌을 가지고 있는 경우, 실제 체육복이 있다고 판단하고 여벌은 없다고 판단
            reserve.remove(person)      # 여벌 체육복을 가지고 있는 사람 리스트에서 제거
        else:
            real_lost.append(person)    # 아닐 경우, 진짜 체육복을 도난당한 사람 리스트에 추가
    answer = n-len(real_lost)           # 전체 사람 수에서 진짜 체육복을 도난당한 사람을 뺀 자기 체육복을 가지고 있는 사람 수
    real_lost.sort()                    # 도난 당한 사람들이 앞사람의 여벌 유무를 우선 체크하고 뒷사람을 체크하는 매커니즘을 모두 적용하여 최대 체육 수업 참여 가능한 사람을 구하기 위하여 정렬
                                        # 만약 정렬되어 있지 않은 경우, 정렬되지 않은 가운데 번호 사람이 먼저 해당 매커니즘을 적용 받아 앞사람은 해당 매커니즘을 적용하지 못하는 경우 발생
    for person in real_lost:            # 먼저 앞사람 여별복 유무를 판단하고 뒷사람을 판단하여 여벌복을 빌리는 매커니즘 적용
        if person-1 in reserve:         # 앞사람 여벌복 유무 체크
            reserve.remove(person-1)    # 여벌복을 빌릴 경우, 여벌복을 가지고 있는 리스트에서 해당 사람을 제거
            answer += 1                 # 체육 수업 참여 가능 수 추가
        elif person+1 in reserve:       # 뒷사람 여벌복 유무 체크
            reserve.remove(person+1)    # 여벌복을 빌릴 경우, 여벌복을 가지고 있는 리스트에서 해당 사람을 제거
            answer += 1                 # 체육 수업 참여 가능 수 추가
    return answer