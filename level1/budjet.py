"예산"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12982"

def solution(d, budget):
    answer = 0                  # 선택한 부서 수 초기화
    total_cost = 0              # 선택한 부서들의 총 비용 초기화
    d.sort()                    # 부서별 신청 금액 오름차순 정렬
    for cost in d:              # 신청 금액이 작은 부서별로 탐색 시작
        total_cost += cost      # 부서별 신청 금액을 총비용에 추가
        if total_cost > budget: # 총비용이 예산을 초과할 경우,
            break               # 마지막으로 선택한 부서를 빼고 반복문 탈출
        answer += 1             # 부서를 추가
    return answer