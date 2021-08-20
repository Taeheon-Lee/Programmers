"하샤드 수"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12947"

def solution(x): 
    return True if x % sum(map(int, str(x))) == 0 else False