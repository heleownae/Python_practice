# 자연수 뒤집어 배열로 만들기 (1) - 리스트 컴프리헨션

def solution(n):
    
    return [int(i) for i in reversed(str(n))]


# 자연수 뒤집어 배열로 만들기 (2)

def solution(n):
    
    num_str = str(n)                # str(): 숫자를 문자열로 변환하여 변수에 저장
    answer = []
    
    for i in reversed(num_str):     # reversed(): 문자열을 역순으로, for문: 반복
        answer.append(int(i))
        
    return answer


# 자연수 뒤집어 배열로 만들기 (3)

def solution(n):
    
    answer = []
    
    while True:
        answer.append(n % 10)
        n //= 10                # //: 나눗셈을 한 후에 정수 부분만 반환하는 연산자
        
        if n == 0:
            break
    
    return answer