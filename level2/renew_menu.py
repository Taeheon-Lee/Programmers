"메뉴 리뉴얼"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/72411"

import itertools

def solution(orders, course):
    orders = ["".join(sorted(list(elem))) for elem in orders]                                                   # 주문 리스트를 오름차순 메뉴 순서로 정렬
    answer = []
    for num in course:
        dic = {}                                                                                                # 각 세트 메뉴 후보를 담을 딕셔너리 생성
        candidate_lst = [list(map(lambda x:"".join(x), itertools.combinations(elem, num))) for elem in orders]  # 각 손님별로 후보 세트 메뉴 리스트 생성
        for customer in candidate_lst:                                                                          # 각 손님별로
            cnt = 0                                                                                             # 후보 세트 메뉴 주문 횟수 초기화
            for set_menu in customer:                                                                           # 손님이 시킨 단품메뉴 조합을 바탕으로 한 세트 후보 메뉴 중에서
                if set_menu in dic.keys():                                                                      # 후보 딕셔너리에 이미 존재하는 경우, 확인한 메뉴이기 때문에 pass
                    continue
                for history in candidate_lst:                                                                   # 존재하지 않는 경우
                    if set_menu in history:                                                                     # 선택한 세트 메뉴가 손님들이 시켰던 단품 메뉴들에 존재할 경우,
                        cnt += 1                                                                                # 시킨 횟수 + 1
                dic[set_menu] = cnt                                                                             # 해당 후보 메뉴와 시킨 횟수를 딕셔너리에 추가
                cnt = 0                                                                                         # 후보 세트 메뉴 주문 횟수 초기화
        if len(dic.values()) != 0 and max(list(dic.values())) > 1:                                              # 후보 세트 메뉴가 존재하고 메뉴들 중 최대 주문 횟수가 2회 이상인 것이 있을 경우,
            select_standard = max(list(dic.values()))                                                           # 후보 세트 메뉴 중 가장 많이 주문한 세트 메뉴의 주문 횟수 확인
            for menu in list(dic.keys()):                                                                       # 각 후보 세트 메뉴들 중
                if dic[menu] == select_standard:                                                                # 가장 많이 주문한 세트 메뉴 주문 횟수와 동일한 세트 메뉴를 answer 리스트에 추가
                    answer.append(menu)
    return sorted(answer)                                                                                       # 알파벳 순으로 정렬하여 리턴
