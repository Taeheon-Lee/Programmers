"신규 아이디 추천"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/72410"

import re

def solution(new_id):
    new_id = new_id.lower()                                 # 1 단계
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)             # 2 단계 (^은 "not"의미, 리스트로 묶을 경우 그룹으로 처리 가능)
    new_id = re.sub('\.+', '.', new_id)                     # 3 단계 (.앞에 \를 붙일 경우, 해당 문자 매칭만 치환, *은 0번 이상 매칭, +는 1번 이상 매칭)
    new_id = re.sub('^[.]|[.]$', '', new_id)                # 4 단계 ($은 마지막을 의미, |는 "or" 의미)
    new_id = 'a' if len(new_id) == 0 else new_id            # 5 단계
    new_id = new_id[:15] if len(new_id) > 15 else new_id    # 6 단계
    new_id = re.sub('^[.]|[.]$', '', new_id)
    if len(new_id) <= 2:                                    # 7 단계
        while len(new_id) != 3:
            new_id += new_id[-1]
    return new_id