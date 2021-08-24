"괄호 변환"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/60058"

def solution(p):
    answer = ''
    if len(p) == 0:                                     # p가 빈문자열일 경우, 그대로 리턴
        return p
    left, right, i, check = 0, 0, 0, 0                  # "(", ")", "p를 탐색할 인덱스", "올바른 문자열인지 확인" 변수 초기화
    correct = True                                      # 기본값은 "올바른 문자열임"으로 초기화
    while left == 0 or (left > 0 and left != right):    # 더이상 분리할 수 없는 균형잡힌 괄호 문자열로 분할하기 위하여 탐색
        if p[i] == "(":                                 # 처음부터 탐색하여 "(", ")"이 처음으로 같아지는 지점이 더이상 분리할 수 없는 균형잡힌 괄호 문자열을 뽑아낼 인덱스
            left += 1
            check -= 1                                  # "("일 경우, 올바른 문자열인지 확인할 변수를 -1
        elif p[i] == ")":
            right += 1
            check += 1                                  # ")"일 경우, 올바른 문자열인지 확인할 변수 +1
            if check > 0:                               # 만약 확인 변수가 양수로 될 경우는 시작이 ")"이거나 "("가 나타낸 횟수보다 ")"가 더많이 나타난 불균형 괄호 문자열이라는 뜻
                correct = False                         # 문자열이 올바르지 않음으로 변경
        i += 1
    u, v = p[:i], p[i:]                                 # 균형잡힌 문자열을 뽑아낼 인덱스를 기준으로 분리
    if not correct:                                     # 균형잡힌 문자열이 올바르지 않은 문자열일 경우
        tmp = ""
        for elem in u[1:len(u)-1]:
            tmp += ")" if elem == "(" else "("          # 균형잡혔으나 올바르지 않는 문자열을 앞뒤를 제거한 뒤, 괄호의 방향을 모두 뒤집음
        answer = "(" + solution(v) + ")" + tmp          # 인덱스 기준으로 뽑아내고 남은 문자열에 대하여 재귀 수행을 한 뒤, 앞뒤에 "(", ")"을 붙이고 바로 위에서 작업한 뒤집은 문자열을 추가
    else:                                               # 균형잡힌 문자열이 올바른 문자열인 경우
        answer = u + solution(v)                        # 인덱스 기준으로 뽑아내고 남은 문자열에 대하여 재귀 수행을 하여 뒤에 붙임
    return answer