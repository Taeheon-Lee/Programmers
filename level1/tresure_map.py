"비밀 지도"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/17681"

def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = bin(arr1[i]|arr2[i])[2:].replace("1","#").replace("0"," ")    # & 연산은 두개의 정수를 2진수로 변환하여 and 매칭, | 연산은 or 매칭
        answer.append((n-len(tmp))*" "+tmp)                                 # 결과 값이 지도의 길이보다 작을 경우, 빈 공간을 " "을 추가
    return answer