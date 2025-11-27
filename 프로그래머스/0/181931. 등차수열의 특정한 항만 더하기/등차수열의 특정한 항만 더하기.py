def solution(a, d, included):
    answer = 0
    for idx, flag in enumerate(included):   
        if flag:                            
            term = a + d * idx              
            answer += term
    return answer