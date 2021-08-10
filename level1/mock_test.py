"모의고사"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/42840"

def solution(answers):
    pattern_1st = [1, 2, 3, 4, 5]                       # 1번 수포자 정답 패턴
    pattern_2nd = [2, 1, 2, 3, 2, 4, 2, 5]              # 2번 수포자 정답 패턴
    pattern_3rd = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]        # 3번 수포자 정답 패턴
    
    total_score = [0, 0, 0]                             # 각 수포자들의 종합 점수 리스트
    rank = []                                           # 출력 값을 저장할 순위 리스트
    
    for i, num in enumerate(answers):                   # 각 번호의 정답 확인
        if num == pattern_1st[i % len(pattern_1st)]:
            total_score[0] += 1
        if num == pattern_2nd[i % len(pattern_2nd)]:
            total_score[1] += 1
        if num == pattern_3rd[i % len(pattern_3rd)]:
            total_score[2] += 1
            
    for i in range(len(total_score)):                   # 가장 높은 값을 받은 사람을 차례대로 순위 리스트에 삽입
        if total_score[i] == max(total_score):          # 동점일 경우, 이미 오름차순 순서대로 확인하고 있기 때문에 정렬할 필요가 없음
            rank.append(i + 1)
    
    return rank