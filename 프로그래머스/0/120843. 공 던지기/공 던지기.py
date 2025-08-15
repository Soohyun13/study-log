def solution(numbers, k):
    even_index = []
    while k > len(even_index):
        numbers += numbers
        even_index = numbers[0::2]
    return even_index[k-1]
    