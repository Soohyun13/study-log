def solution(citations):
    answer = 0
    # 총 5편의 논문
    # 1번 이상 인용된 논문 개수: 4
    # 2번 이상 인용된 논문 개수: 3
    # 3번 이상 인용된 논문 개수: 3 -> 인용 횟수 >= 논문 개수인 인용 횟수의 최댓값
    # 4번 이상 인용된 논문 개수: 2
    # 5번 이상 인용된 논문 개수: 2
    # 6번 이상 인용된 논문 개수: 1
    for h in range(0, max(citations)+1):
        count = 0
        for citation in citations:        
            if citation >= h:              
                count += 1
        if count >= h:                    
            answer = max(answer, h)         
    return answer