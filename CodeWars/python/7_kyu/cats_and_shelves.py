# https://www.codewars.com/kata/62c93765cef6f10030dfa92b

def solution(start: int, finish: int) -> int:
    steps = 0
    current = start
    while current < finish:
        if current + 3 > finish:
            current += 1
        else:
            current += 3
        steps += 1
    return steps
