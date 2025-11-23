def solution(myString):
    lower_myString = myString.lower()
    if 'a' in lower_myString:
        return lower_myString.replace('a', 'A')
    return lower_myString