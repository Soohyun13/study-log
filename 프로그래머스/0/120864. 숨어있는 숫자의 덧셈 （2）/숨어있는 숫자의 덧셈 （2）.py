import re
def solution(my_string):
    numbers = re.findall(r"[0-9]+", my_string)
    answer = sum(int(n) for n in numbers)
    return answer