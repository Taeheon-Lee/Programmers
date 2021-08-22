"오픈채팅방"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/42888"

def solution(record):
    answer = []
    dic = {}                                                # 접속 아이디를 저장할 딕셔너리 생성
    for elem in record:
        elem = list(elem.split())                           # 리스트화
        if elem[0] == "Enter":                              # 접속한 경우
            dic[elem[1]] = elem[2]                          # 접속 아이디를 딕셔너리에 입력, 기존에 있는 경우에는 수정
            answer.append([elem[1], "님이 들어왔습니다."])  # 최종 수정 정보를 반영하기 위하여 우선 아이디 값으로 접속 정보를 저장    
        elif elem[0] == "Change":                           # 변경한 경우
            dic[elem[1]] = elem[2]                          # 딕셔너리에서 해당 아이디 정보를 업데이트
        else:                                               # 나간 경우
            answer.append([elem[1], "님이 나갔습니다."])    # 최종 수정 정보를 반영하기 위하여 우선 아이디 값으로 퇴장 정보를 저장
    for i in range(len(answer)):
        answer[i] = dic[answer[i][0]] + answer[i][1]        # 최종 딕셔너리 정보로 로그 정보를 answer 리스트에 저장
    return answer