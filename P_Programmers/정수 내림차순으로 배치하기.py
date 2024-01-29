# 정수 내림차순으로 배치하기

def solution(n):
    
    order = sorted(str(n), reverse=True)
    number = ''.join(order)
        
    return int(number)