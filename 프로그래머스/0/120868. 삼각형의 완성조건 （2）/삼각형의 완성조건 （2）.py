def solution(sides):
    a, b = sides
    big = max(a, b)
    small = min(a, b)
    return (a + b - big - 1) + small