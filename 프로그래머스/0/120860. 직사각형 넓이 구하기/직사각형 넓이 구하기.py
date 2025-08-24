def solution(dots):
    x_list = [x for x, y in dots]
    y_list = [y for x, y in dots]
    w = max(x_list) - min(x_list)
    h = max(y_list) - min(y_list)
    return w * h