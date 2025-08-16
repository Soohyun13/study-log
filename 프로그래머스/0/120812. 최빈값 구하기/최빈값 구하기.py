from collections import Counter

def solution(array):
    counts = Counter(array)
    max_count = max(counts.values())
    modes = [key for key, value in counts.items() if value == max_count]
    
    if len(modes) >= 2:
        return -1
    else:
        return modes[0]