def solution(score):
    answer = []
    average_score = []
    for s in score:
        average_score.append(sum(s)/2)
    sorted_average_score = sorted(average_score, reverse=True)
    
    rank = []
    for i in average_score:
        rank.append(sorted_average_score.index(i)+1)
        
    return rank