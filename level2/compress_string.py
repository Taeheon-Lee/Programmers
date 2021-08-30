"문자열 압축"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/60057"

def solution(s):
    lst = [len(s)]                                      # 자르는 개수를 0으로 할 경우, 문자열 그대로이기 때문에 문자 길이 그대로 저장
    for cut in range(1, len(s)//2+1):                   # 문자 자르는 개수가 반이 넘어갈 경우, 자르는 것이 불가능하기 때문에 문자열 자르는 개수를 반보다 작을 때까지 탐색
        total_length = 0                                # 각 자르는 개수마다 총 길이를 넣을 변수 초기화
        tmp = s[:cut]                                   # 첫 비교 문자열
        count = 1                                       # 비교 문자열 다음부터 체크하기 때문에 비교 문자열 개수 하나를 카운트한 뒤 시작
        for i in range(cut, len(s), cut):               # 비교 문자열 다음부터 자르는 개수만큼 간격을 이동하며 체크
            if s[i:i+cut] == tmp:                       # 자른 문자열이 비교 문자열과 동일할 경우,
                count += 1                              # 1 카운트
            else:                                       # 다를 경우,
                if count == 1:                          # 카운트 수가 1일 경우, 뒤에 동일한 문자열이 없다는 것이기 때문에 문자열을 압축하지 않음
                    total_length += cut                 # 총 개수에 자른 문자열 길이만큼 더함
                else:                                   # 1보다 클 경우, 압축 가능하기 때문에
                    total_length += (len(str(count))+cut)    # 압축 개수가 10이상일 경우 2자리 수이기 때문에 문자열로 변환하여 숫자 길이와 자른 문자열 길이를 총 개수에 더함
                tmp = s[i:i+cut]                        # 비교 문자열을 해당 위치에서 자른 문자열로 새롭게 변경
                count = 1                               # 비교 문자열 다음부터 체크하기 때문에 다시 카운트를 1로 초기화
            if i == len(s)-cut:                         # 현재 위치가 마지막 위치이고 더 자를 수 있는 경우, 탐색을 종료하고 카운트를 체크해야 하기 때문에 카운트를 총 길이에 반영
                if count == 1:
                    total_length += cut
                else:
                    total_length += (len(str(count))+cut)
            elif i > len(s)-cut:                        # 현재 위치가 마지막 위치이고 더 자를 수 없는 경우, 나머지는 압축이 불가능하기 때문에 그대로 길이만큼 총 길이에 추가
                total_length += len(s[i:])
        lst.append(total_length)                        # 총 길이를 정답 리스트에 추가
    return min(lst)                                     # 정답 리스트에서 가장 작은 경우의 길이를 반환
