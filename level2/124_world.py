"124 나라의 숫자"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12899"

def solution(n):
    num_lst = ['1', '2', '4']
    answer = ''
    n -= 1                                  # 인덱스는 0부터 시작하기 때문에 -1
    while (n >= 3):                         # n이 3보다 크거나 같은 경우, 즉 4 이상인 경우,
        answer = num_lst[n % 3] + answer    # 3으로 나눈 나머지 값을 마지막 자리수로 사용
        n = n // 3 - 1                      # 3으로 나눈 몫을 사용하되 인덱스를 고려하여 -1
    answer = num_lst[n % 3] + answer        # 3 이하의 남은 수도 1,2,4 중 하나로 반영
    return answer