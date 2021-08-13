"카패드 누르기"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/67256"

dic_loc = {"left":[1,4,7],"right":[3,6,9],"middle":[2,5,8,0]}                                                   # 위치 딕셔너리
dic_dis_2 = {1:1,2:0,3:1,4:2,5:1,6:2,7:3,8:2,9:3,0:3,'*':4,'#':4}                                               # 2 키버튼 기준 각 버튼의 거리
dic_dis_5 = {1:2,2:1,3:2,4:1,5:0,6:1,7:2,8:1,9:2,0:2,'*':3,'#':3}                                               # 5 키버튼 기준 각 버튼의 거리
dic_dis_8 = {1:3,2:2,3:3,4:2,5:1,6:2,7:1,8:0,9:1,0:1,'*':2,'#':2}                                               # 8 키버튼 기준 각 버튼의 거리
dic_dis_0 = {1:4,2:3,3:4,4:3,5:2,6:3,7:2,8:1,9:2,0:0,'*':1,'#':1}                                               # 0 키버튼 기준 각 버튼의 거리

def solution(numbers, hand):
    answer = ''                                                                                                 # 정답 문자열
    left_loc = '*'                                                                                              # 왼손 위치 초기화
    right_loc = '#'                                                                                             # 오른손 위치 초기화
    for key in numbers:
        if key in dic_loc["left"]:                                                                              # 눌러야할 버튼이 왼쪽 위치일 경우
            answer += "L"
            left_loc = key                                                                                      # 왼손 위치를 해당 키로 이동
        elif key in dic_loc["right"]:                                                                           # 눌러야할 버튼이 오른쪽 위치일 경우
            answer += "R"
            right_loc = key                                                                                     # 오른손 위치를 해당 키로 이동
        else:                                                                                                   # 눌러야할 버튼이 중간 위치일 경우
            dic = dic_dis_2 if key == 2 else dic_dis_5 if key == 5 else dic_dis_8 if key == 8 else dic_dis_0    # 키에 따라 딕셔너리 선택
            if dic[left_loc] < dic[right_loc]:                                                                  # 왼손 거리값이 오른손 거리값보다 작은 경우
                    answer += "L"
                    left_loc = key                                                                              # 왼손 위치를 해당 키로 이동
            elif dic[left_loc] > dic[right_loc]:                                                                # 오른손 거리값이 왼손 거리값보다 작은 경우
                    answer += "R"
                    right_loc = key                                                                             # 오른손 위치를 해당 키로 이동
            else:                                                                                               # 양손의 거리값이 같은 경우
                if hand == "right":                                                                             # 오른손 잡이일 경우
                    answer += "R"
                    right_loc = key                                                                             # 오른손 위치를 해당 키로 이동
                else:                                                                                           # 왼손 잡이일 경우
                    answer += "L"
                    left_loc = key                                                                              # 왼손 위치를 해당 키로 이동
    return answer