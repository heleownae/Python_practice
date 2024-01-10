# 올바른 괄호

# list 자료형으로 stack을 유사하게 구현 (LIFO)
# 문자열 s를 반복해서 확인
# 열린 괄호 - 일단 stack에 넣기
# 닫힌 괄호 - 현재 stack에 들어 있는 최상단 자료와 비교하여 쌍이 되면 pop

def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True