def solution(numbers):
    answer = 0
    numbers.sort()
    for n in numbers:
        answer = numbers[-1] * numbers[-2]
    return answer