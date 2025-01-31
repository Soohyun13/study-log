def solution(array, commands):
    answer = []
    for i, j , k in commands:
        sliced_array = array[i-1:j]
        sorted_array = sorted(sliced_array)
        number = sorted_array[k-1]
        answer.append(number)
    return answer