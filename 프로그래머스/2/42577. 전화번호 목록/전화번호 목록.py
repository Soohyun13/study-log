def solution(phone_book):
    phone_book.sort() # 문자열 정렬은 사전 순
                      # 접두어가 먼저 나오고, 그걸 포함하는 긴 문자열이 바로 뒤에 붙는 구조
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True