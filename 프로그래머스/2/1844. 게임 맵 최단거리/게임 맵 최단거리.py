from collections import deque

def solution(maps): 
    n, m = len(maps), len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0,0))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == m-1:
            return maps[x][y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
                    
    return -1