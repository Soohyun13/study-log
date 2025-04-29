def solution(participant, completion):
    hash_table = {}
    for p in participant:
        hash_table[p] = hash_table.get(p, 0) + 1
    for c in completion:
        hash_table[c] -= 1
    for p in hash_table:
        if hash_table[p] > 0:
            answer = p
    return answer