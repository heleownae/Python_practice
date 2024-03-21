# K번째수
def solution(array, commands):
    answer = []
    for a, b, c in commands:
        # a~b 자르고 -> 오름차순 정렬 -> 정렬한 배열의 c번째 숫자
        answer.append(sorted(array[a-1:b])[c-1])
    return answer