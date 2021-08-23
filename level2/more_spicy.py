"더 맵게"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/42626"

import heapq                                                            # 힙 자료구조 사용

def solution(scoville, K):
    answer = 0                                                          # 섞는 횟수 초기화
    heapq.heapify(scoville)                                             # 기존 리스트를 힙 자료구조료 변형
    while scoville[0] < K:                                              # 인덱스 0에 가장 작은 값이 들어가기 때문에 가장 작은 값이 K보다 클 때까지 반복
        new_food = heapq.heappop(scoville) + heapq.heappop(scoville)*2  # 스코빌 지수가 가장 낮은 값 두개를 추출하여 섞은 뒤 새로운 음식으로 만듬
        heapq.heappush(scoville, new_food)                              # 해당 음식을 scoville 힙에 추가
        answer += 1                                                     # 섞은 횟수 1추가
        if len(scoville) == 1 and scoville[0] < K:                      # 만약 모든 음식을 섞어도 스코빌 지수가 K보다 낮은 경우
            return -1                                                   # -1 리턴
    return answer                                                       # 섞은 횟수 리턴