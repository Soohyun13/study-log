def solution(polynomial):
    x = 0
    c = 0
    
    polynomial = polynomial.split(" + ")
    for i in polynomial:
        if i.endswith('x'):
            x += int(i[:-1]) if len(i) > 1 else 1
        else:
            c += int(i)
    
    if x and c:
        return ("x" if x == 1 else f"{x}x") + f" + {c}"
    elif x:
        return "x" if x == 1 else f"{x}x"
    else:
        return str(c)