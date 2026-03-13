from collections import Counter
def solution(participant, completion):
    answer = ''

    answer = list((Counter(participant) - Counter(completion)).elements())[0]
    return answer

# Counter -> 등장 횟수도 같이 저장, 값의 개수를 저장하는 딕셔너리
# elements로 리스트로 복구
