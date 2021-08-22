"오픈채팅방"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/42888"

def solution(record):
    answer = []
    dic = {}
    for elem in record:
        elem = list(elem.split())
        if elem[0] == "Enter":
            dic[elem[1]] = elem[2]
            answer.append([elem[1], "님이 들어왔습니다."])
        elif elem[0] == "Change":
            dic[elem[1]] = elem[2]
        else:
            answer.append([elem[1], "님이 나갔습니다."])
    for i in range(len(answer)):
        answer[i] = dic[answer[i][0]] + answer[i][1]
    return answer