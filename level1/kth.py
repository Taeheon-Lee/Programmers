"k번째수"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/42748"

def solution(array, commands):
    answer = []
    for elem in commands:
        tmp = sorted(array[:][elem[0]-1:elem[1]])   # 배열을 복제하는 것은 단순히 새로운 변수에 배열을 집어넣는 방식으로 수행할 수 없음
                                                    # 단순히 새로운 변수에 배열을 넣는 경우, 해당 주소값이 넘어가는 것으로 새로운 변수를 조작하면 결국 기존의 배열 또한 수정이 일어남
                                                    # 배열을 복제하는 것은 "새로운 변수 = 배열[:]"으로 복제 가능하며, 슬라이싱을 통하여 배열을 자를 수 있음
        answer.append(tmp[elem[2]-1])               # 정렬된 잘린 배열의 k번째를 정답 리스트에 추가
    return answer