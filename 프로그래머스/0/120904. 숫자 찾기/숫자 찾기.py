def solution(num, k):
    str_num = str(num)
    for i in range(len(str_num)):
        if str_num[i] == str(k):
            return i+1
    return -1