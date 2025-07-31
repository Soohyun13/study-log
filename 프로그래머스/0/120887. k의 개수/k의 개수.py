def solution(i, j, k):
    k = str(k)
    answer = 0
    for num in range(i, j+1):
        answer += str(num).count(k)
    return answer