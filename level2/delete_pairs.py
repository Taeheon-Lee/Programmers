"짝지어 제거하기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/12973"

def solution(s):
    stack = []                                      # 스택 사용
    for i in range(len(s)):                         # for문을 이용하여 인덱스 탐색, 초기에 리스트로 만들어 while문과 pop을 이용하였으나 시간 초과 발생
        if len(stack) == 0 or stack[-1] != s[i]:    # 스택에 아무것도 없거나 마지막 스택의 문자가 현재 넣을 문자와 다를 경우
            stack.append(s[i])                      # 현재 문자를 스택에 삽입
        else:                                       # 마지막 스택의 문자가 현재 넣은 문자와 동일할 경우
            stack.pop(-1)                           # 같은 두개를 제거해야 하기 때문에 스택의 마지막 문자를 삭제
    if len(stack) == 0:                             # 탐색 완료 후, 스택에 값이 없을 경우, 모두 삭제된 경우로 1 리턴
        return 1
    return 0                                        # 아닐 경우, 제거되지 못하는 문자가 있는 것으로 0 리턴