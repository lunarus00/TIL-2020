function solution(numbers, target) {
    var answer = 0;
    function find_nums(numbers, target, answer, now_here, now_sum) {
        if (now_here == numbers.length){
            if (now_sum == target){
                answer++;
                return answer
            } else {
                return answer
            }
        }
        for (var i = 0; i<2; i++) {
            if (i == 0) {
                now_sum = now_sum + numbers[now_here];
                now_here++;
                answer = find_nums(numbers, target, answer, now_here, now_sum);
                now_here--;
                now_sum = now_sum - numbers[now_here];
            } else {
                now_sum = now_sum - numbers[now_here];
                now_here++;
                answer = find_nums(numbers, target, answer, now_here, now_sum);
                now_here--;
                now_sum = now_sum + numbers[now_here];
            }
        }
        return answer
    }
    var now_here = 0;
    var now_sum = 0;
    answer = find_nums(numbers, target, answer, now_here, now_sum);
    return answer;
}