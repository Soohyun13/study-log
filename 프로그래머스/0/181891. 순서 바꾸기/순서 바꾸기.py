def solution(num_list, n):
    answer = []
    n_list_1 = num_list[n:]
    n_list_2 = num_list[:n]
    answer = n_list_1 + n_list_2
    return answer