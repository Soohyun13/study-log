def solution(array):
    answer = []
    sorted_array = sorted(array)
    max_number = max(sorted_array)
    answer.append(max_number)
    for i in range(len(array)):
        if array[i] == max_number:
            answer.append(i)
    return answer