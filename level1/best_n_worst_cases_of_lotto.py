"로또의 최고 순위와 최저 순위"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3"

def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]                          # 순위를 정하기 위해 배열을 사용
    cnt = 0                                         # 몇 개를 맞추었는지 세기 위하여 cnt 변수 사용, 초기화
    for elem in lottos:                             # 로또 번호를 순서대로 탐색
        if elem in win_nums:                        # 로또 번호가 당첨 번호와 일치한다면 cnt + 1
            cnt += 1
    return [rank[cnt+lottos.count(0)], rank[cnt]]   # 맞춘 번호 이와의 지워진 번호가 다 맞은 경우가 최고 순위, 다 틀린 경우가 최저 순위