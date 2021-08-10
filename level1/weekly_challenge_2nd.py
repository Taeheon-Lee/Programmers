"위클리 챌린지 2주차"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/83201"

def solution(scores):
    answer = ""                                                             # 출력 값을 저장할 문자열 생성
    length = len(scores)                                                    # 행과 열의 길이
    
    for col in range(length):                                               # 탐색 시작
        lst = []                                                            # 각 학생의 점수를 저장할 리스트 생성
        for row in range(length):
            lst.append(scores[row][col])                                    # 각 학생의 점수를 리스트에 저장
            
        if lst.count(lst[col]) == 1 and (lst[col] in [min(lst), max(lst)]): # 조건 확인
            del(lst[col])                                                   # 조건에 맞지 않을 경우 점수 제거
            
        check_score = sum(lst)/len(lst)                                     # 각 학생의 점수 평균
        
        if check_score >= 90:                                               # 조건에 따라 학점 부여
            answer += "A"
        elif check_score >= 80:
            answer += "B"
        elif check_score >= 70:
            answer += "C"
        elif check_score >= 50:
            answer += "D"
        else:
            answer += "F"

    return answer                                                           # 결과 값 출력