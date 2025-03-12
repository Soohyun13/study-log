def solution(sides):
    if max(sides)*2 < sum(sides):
        answer = 1
    else:
        answer = 2
    return answer