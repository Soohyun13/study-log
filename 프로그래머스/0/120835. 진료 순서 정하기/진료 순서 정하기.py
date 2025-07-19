def solution(emergency):
    sorted_emg = sorted(emergency, reverse=True)
    ranks = {num: i+1 for i, num in enumerate(sorted_emg)}
    return [ranks[num] for num in emergency]
