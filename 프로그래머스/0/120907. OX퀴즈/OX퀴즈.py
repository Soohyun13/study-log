def solution(quiz):
    answer = []
    for i in quiz:
        left, right = i.split(' = ')
        if eval(left) == int(right):
            answer.append('O')
        else:
            answer.append('X')
    return answer