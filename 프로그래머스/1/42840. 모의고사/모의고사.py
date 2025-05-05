def solution(answers):
    score_1 = 0
    score_2 = 0
    score_3 = 0
    
    list_1 = [1,2,3,4,5]
    list_2 = [2,1,2,3,2,4,2,5]
    list_3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        pick_1 = list_1[i % len(list_1)]
        pick_2 = list_2[i % len(list_2)]
        pick_3 = list_3[i % len(list_3)]
        
        if answers[i] == pick_1:
            score_1 += 1
        if answers[i] == pick_2:
            score_2 += 1
        if answers[i] == pick_3:
            score_3 += 1
        
    max_score = max(score_1, score_2, score_3)
    answer = []
    if score_1 == max_score:
        answer.append(1)
    if score_2 == max_score:
        answer.append(2)
    if score_3 == max_score:
        answer.append(3)
                
    answer.sort()
    return answer