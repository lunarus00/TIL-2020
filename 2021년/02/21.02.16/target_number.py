def solution(numbers, target):
    answer = 0
    def find_sum(numbers, check_sum, count_try, answer, target):
        if count_try == len(numbers):
            if check_sum == target:
                answer += 1
                return answer
            return answer
        for i in range(2):
            if i == 0:
                check_sum += numbers[count_try]
                count_try += 1
                answer = find_sum(numbers, check_sum, count_try, answer, target)
                count_try -= 1
                check_sum -= numbers[count_try]
            else:
                check_sum -= numbers[count_try]
                count_try += 1
                answer = find_sum(numbers, check_sum, count_try, answer, target)
                count_try -= 1
                check_sum += numbers[count_try]
        return answer
    count_try = 0
    check_sum = 0
    answer = find_sum(numbers, check_sum, count_try, answer, target)
    return answer