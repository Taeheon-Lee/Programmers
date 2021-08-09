"위클리 챌린지 2주차"

# 대학 교수인 당신은, 상호평가를 통하여 학생들이 제출한 과제물에 학점을 부여하려고 합니다.
# 2차원 행렬 점수표 scores[i][j]에서 i행 j열의 값은 i번 학생이 평가한 j번 학생의 과제 점수입니다.
# 당신은 각 학생들이 받은 점수의 평균을 구하여, 기준에 따라 학점을 부여하려고 합니다.
# 만약, 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면 그 점수는 제외하고 평균을 구합니다.
# 제외할 점수는 제외하고 평균을 구한 후, 아래 기준에 따라 학점을 부여합니다.
# 90점 이상 "A"
# 90점 미만 80점 이상 "B"
# 80점 미만 70점 이상 "C"
# 70점 미만 50점 이상 "D"
# 50점 미만 "F"

# 예시
# 입력 값 : [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
# 출력 값 : "FBABD"

# 제한 사항
# 2 ≤ scores의 행의 길이(학생 수) ≤ 10
# scores의 열의 길이 = scores의 행의 길이 (즉, scores는 행과 열의 길이가 같은 2차원 배열입니다.)
# 0 ≤ scores의 원소 ≤ 100
# 0번 학생의 학점부터 차례대로 이어 붙인 하나의 문자열을 return 합니다.

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