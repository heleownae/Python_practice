def solution(arr, divisor):
    answer = []
    
    # for 반복을 통한 연산
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    # 예외 처리
    if len(answer) == 0:
        answer = [-1]
    
    # 오름차순 정렬
    return list(sorted(answer))


# 문제 이해 > 어떻게 로직 세울지 고민 > 코딩으로 구현

# 1. 각 array의 element 중 divisor로 나누어 떨어지는 값
#    = array 속 각 element에 divisor 연산을 하는구나. 하나하나. 그럼 for문 쓰겠군

# 2. 오름차순으로 정렬

# 3. 나누어 떨어지는 게 없다면, -1 반환
#    = if문 쓰겠구나, 예외처리가 있겠구나

# 제한사항
# 
# 자연수 - divison by zero 에러가 있는데 이건 굳이 예외처리할 필요가 없구나.
# array - 비어 있는 배열이 들어오진 않는다.