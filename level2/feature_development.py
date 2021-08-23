"기능개발"

# 문제 링크 "https://programmers.co.kr/learn/courses/30/lessons/42586"

def solution(progresses, speeds):                                   # 큐 자료구조 특징 사용
    answer = []
    while len(progresses) != 0:
        progresses = [x+y for x, y in zip(progresses, speeds)]      # 각 작업 속도를 각 작업 진도에 더함
        if progresses[0] >= 100:                                    # 첫 번쨰 작업이 100% 이상이 될 경우,
            cnt = 0                                                 # 배포 개수 초기화
            while len(progresses) != 0 and progresses[0] >= 100:    # 가장 앞에 있는 작업과 연속된 작업 진도가 100%인 작업을 배포하고 배포 개수를 추가 
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            answer.append(cnt)                                      # 배포 개수를 answer 리스트에 추가
    return answer