def solution(num_list):
    multi = 1
    plus = 0
    for i in num_list:
        multi *= i
        plus += i
    return 1 if multi < plus **2 else 0