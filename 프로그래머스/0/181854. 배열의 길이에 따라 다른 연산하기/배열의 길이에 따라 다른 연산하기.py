def solution(arr, n):
    answer = []
    if len(arr) % 2 != 0: # arr의 길이가 홀수
        for i in range(len(arr)):
            if i % 2 == 0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    else: # arr의 길이가 짝수
        for i in range(len(arr)):
            if i % 2 != 0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    return answer