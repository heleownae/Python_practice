# 자릿수 더하기
def solution(n):
    digit_sum = 0
    
    while n > 0:
        digit_sum += n % 10
        n //= 10
        
    return digit_sum