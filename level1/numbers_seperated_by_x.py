"x만큼 간격이 있는 n개의 숫자"

# 문제 링크 ""

def solution(x, n):
    # 음수일 경우, 뒤로 가면서 빠지기 때문에 끝 값에 -1
    # 양수일 경우, 앞로 가면서 더해지기 때문에 끝 값에 +1
    return [i for i in range(x, n*x+1 if x >= 0 else n*x-1, x)] if x != 0 else [0]*n