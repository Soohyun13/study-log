def solution(money):
    answer = []
    coffee = money // 5500
    left_money = money - (5500*coffee)
    answer.append(coffee)
    answer.append(left_money)
    return answer