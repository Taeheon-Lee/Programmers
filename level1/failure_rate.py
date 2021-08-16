"실패율"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/42889"

def solution(N, stages):
    dic = {}                                                                # 스테이지별 실패율을 넣을 딕셔너리 생성
    total_players = len(stages)                                             # 총 플레이어 수
    for st in range(1, N+1):                                                # 스테이지별 탐색
        cnt = 0                                                             # 스테이지를 도달하지 못한 사람 수 초기화
        for player in range (total_players):                                # 플레이어 별 수행 스테이지 탐색
            if stages[player] < st:                                         # 현재 탐색 중인 스테이지를 도달하지 못한 경우,
                cnt += 1                                                    # 스테이지를 도달하지 못한 사람 수 추가
        if cnt == total_players:                                            # 현재 탐색 중인 스테이지를 모두 도달하지 못한 경우,
            dic[st] = 0                                                     # 실패율 0
        else:                                                               # 아닐 경우,
            dic[st] = stages.count(st) / (total_players - cnt)              # 실패율 계산
    answer = sorted(dic.keys(), key = lambda x : dic[x], reverse = True)    # 딕셔너리의 키(스테이지)를 실패율의 기준으로 내림차순 정렬
    return answer