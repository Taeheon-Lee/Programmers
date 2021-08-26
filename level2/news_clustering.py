"뉴스 클러스터링"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/17677"

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]   # 만약 2개씩 자른 문자열이 알파벳으로만 이루어져 있을 경우,
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]   # 해당 문자열을 소문자로 만들고 이 문자열들의 리스트로 변환
    if len(str1) == 0 and len(str2) == 0:                                               # 두개다 공집합일 경우, answer = 1
        answer = 1
    else:                                                                               # 아닐 경우, 교집합과 합집합 계산 (집합 연산은 다중 집합 확장이 불가능하기에 리스트를 이용)
        inter = 0                                                                       # 교집합 갯수를 0으로 초기화
        uni = len(str1) + len(str2)                                                     # 합집합의 갯수를 두 리스트 길이의 합으로 초기화
        for elem in str1:                                                               # 교집합 갯수 탐색
            if elem in str2:                                                            # 교집합일 경우
                inter += 1                                                              # 갯수를 추가
                str2.remove(elem)                                                       # 교집합으로 판단한 원소는 중복을 제거하기 위하여 리스트에서 제거
        uni -= inter                                                                    # 두 리스트의 갯수의 합에서 중복 적용된 교집합 갯수를 뺴면 합집합 갯수
        answer = inter / uni                                                            # 교집합 / 합집합이 answer
    return int(answer*65536)                                                            # 65536을 곱한 뒤 소수점을 제거한 정수로 변환