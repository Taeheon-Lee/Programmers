"폰켓몬"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/1845"

def solution(nums):
    select_num = len(nums) // 2                                     # 선택할 수 있는 포켓몬 수
    types_num = len(set(nums))                                      # 포켓몬 종류 수
    answer = types_num if types_num < select_num else select_num    # 종류 수가 선택 수 보다 적을 경우, 최대 선택 가능 종류는  종류 수와 동일하며, 클 경우 선택 수 만큼 종류 수 획득 가능
    return answer