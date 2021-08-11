import itertools

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12977"

def solution1(nums):
    e = [i for i in range(1, sum(nums)+1)]              # 에라토스테네스의 체 생성
    i = 1
    while i < len(e):                                   # 리스트 내부를 하나씩 순서대로 탐색
        tmp = e[i]
        j = 2
        while tmp*j <= sum(nums):                       # 선택된 값의 배수를 2배수부터 배열에서 모두 제거
            if tmp*j in e:
                e.remove(tmp*j)
            j += 1
        i += 1
    
    case_lst = list(itertools.combinations(nums, 3))    # itertools 패키지에서 조합 생성 함수 사용
    cnt = 0
    for elem in case_lst:                               # 각 조합 케이스의 합이 에라토스테네스의 체 내부에 있을 경우 소수 카운트 1
        if sum(elem) in e:
            cnt += 1 
    return cnt

def solution2(nums):                                    # solution1 보다 속도 우수
    case_lst = list(itertools.combinations(nums, 3))    # itertools 패키지에서 조합 생성 함수 사용
    cnt = 0
    for elem in case_lst:                               # 각 조합 케이스를 순서대로 탐색
        tmp = sum(elem)                                 # 각 케이스의 합
        for n in range(2, tmp//2):                      # 각 케이스의 합이 합의 값보다 작은 어떤 값에 의해 나누어 떨어지는 경우,
            if tmp % n == 0:                            # 합의 반보다 커지는 경우, 절대 나누어 떨어질 수 없으므로 반까지만 탐색
                cnt -= 1                                # cnt 변수를 하나 줄여 이후 cnt가 더해지는 값을 무효화
                break                                   # 더 이상 탐색할 필요가 없기 때문에 반복문을 탈출
        cnt += 1
    return cnt