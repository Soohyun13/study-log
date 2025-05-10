from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])  
    order = 0  

    while queue:
        current = queue.popleft() 
        if any(current[1] < q[1] for q in queue):  
            queue.append(current)
        else:
            order += 1 
            if current[0] == location: 
                return order