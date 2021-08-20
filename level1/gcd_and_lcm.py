"최대공약수와 최소공배수"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12940"

def solution(n, m):
    n1, n2 = max(n, m), min(n, m)   # 두 수를 비교하여 큰 값, 작은 값을 변수로 대입
    i = 1
    while i > 0:                    # 유클리드 호제법 이용 (Euclidean algorithm)
        i = n1 % n2                 # 큰 수에서 작은 수를 나눈 뒤, 다시 작은 수를 나머지로 나누는 작업을 반복하여 나머지가 0이 될 때,
        n1, n2 = n2, i              # 그 수를 나누었던 수가 최대 공약수
    return [n1, int(n*m/n1)]        # 최소 공배수는 두 수의 곱을 두 수의 최대공약수로 나눈 수가 최소 공배수