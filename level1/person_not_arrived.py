"완주하지 못한 선수"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/42576"

def solution(participant, completion):  # 해쉬 값을 이용하지 않을 경우, 시간 초과 발생
    hash_sum = 0                        # 참가자 해쉬 값의 총합을 저장할 변수 생성
    dic = {}                            # 딕셔너리 생성
    for person in participant:
        dic[hash(person)] = person      # 각 참가자의 해쉬 값을 키로 참가자들을 매핑하여 딕셔너리에 저장
        hash_sum += hash(person)        # 해쉬 값을 hash_sum에 더함
    for person in completion:
        hash_sum -= hash(person)        # 각 완주한 사람들의 해쉬 값을 hash_sum에서 뺌
    answer = dic[hash_sum]              # 경기가 종료되고 들어오지 못한 마지막 사람의 해쉬 값을 이용하여 딕셔너리에서 어떤 선수인지 찾아냄
    return answer