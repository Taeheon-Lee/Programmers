"소수 찾기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12921"

def solution(n):                            # 에라토스테네스 체 방식으로 소수 찾기
    a = [False,False] + [True]*(n-1)        # 수를 인덱스로 변환하여 리스트를 이용, 초기 0, 1을 제외한 수를 True로 초기화 
    answer = 0
    for i in range(2,n+1):
        if a[i]:                            # 2부터 해당 수를 소수로 개수에 더함
            answer += 1
            for j in range(2*i, n+1, i):    # 소수의 배수를 False로 만들고 소수에서 제외
                a[j] = False
    return answer