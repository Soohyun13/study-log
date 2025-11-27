def solution(str1, str2):
    answer = ''
    s = len(str1)
    for i in range(s):
        answer += str1[i]+str2[i]
    return answer