def solution(s1, s2):
    answer = 0
    intersection = list(set(s1)&set(s2))
    if intersection != []:
        answer = len(intersection)
    return answer