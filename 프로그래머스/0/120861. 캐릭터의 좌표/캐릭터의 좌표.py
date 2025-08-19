def solution(keyinput, board):
    x, y = 0, 0

    max_x = board[0] // 2
    max_y = board[1] // 2
    
    move = {
        "left":  (-1, 0),
        "right": ( 1, 0),
        "up":    ( 0, 1),
        "down":  ( 0,-1),
    }
    
    for k in keyinput:
        dx, dy = move[k]         
        nx, ny = x + dx, y + dy  
        
        if -max_x <= nx <= max_x and -max_y <= ny <= max_y:
            x, y = nx, ny
    
    return [x, y]