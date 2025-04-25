def solution(array, n):
    answer = 0
    if n in array:
        answer = array.count(n)
    return answer