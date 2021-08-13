"숫자 문자열과 영단어"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/81301"

dic = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

def solution(s):
    answer = s
    for key, value in dic.items():          # items() 함수는 딕셔너리를 key와 value 값의 묶음 리스트로 출력시켜주는 함수
        answer = answer.replace(key, value) # replace("찾을값", "바꿀값", [바꿀횟수])
    return int(answer)