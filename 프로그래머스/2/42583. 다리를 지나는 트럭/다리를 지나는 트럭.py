from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_q = deque([0] * bridge_length)  
    truck_q = deque(truck_weights)        
    time = 0
    current_weight = 0

    while bridge_q:
        time += 1
        out = bridge_q.popleft()           
        current_weight -= out              

        if truck_q:
            if current_weight + truck_q[0] <= weight:
                new_truck = truck_q.popleft()
                bridge_q.append(new_truck)
                current_weight += new_truck
            else:
                bridge_q.append(0)         
    return time
