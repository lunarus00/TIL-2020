def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(1, 10001):
        count_index = 0
        for j in citations:
            if j < i:
                break
            else:
                count_index += 1
            if count_index >= i:
                answer = count_index
                break
    return answer