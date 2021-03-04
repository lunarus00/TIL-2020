function solution(tickets) {
    var answer = [];
    var start = 0;
    var start_check = -1;
    for (var i = 0; i < tickets.length; i++) {
        var start_city = 0;
        var end_city = 0;
        for (var j = 0; j < tickets.length; j++) {
            if (tickets[i][0] == tickets[j][0]) {
                start_city++;
            }
            if (tickets[i][0] == tickets[j][1]) {
                end_city++;
            }
        }
        if (start_city > end_city) {
            if (start_check == -1) {
                start = i;
                start_check = i;
            } else if (tickets[start][0] == tickets[i][0]) {
                if (tickets[start][1] > tickets[i][1]) {
                    start = i;
                }
            } 
        }
    }
    var used = [];
    function find_root(start, used, answer, count_len) {
        if (count_len == 0) {
            answer.push(tickets[start][0]);
        }
        if (count_len == tickets.length) {
            return answer
        }
        var next = 0;
        var next_check = -1;
        used.push(start);
        answer.push(tickets[start][1]);
        count_len++;
        for (var i = 0; i < tickets.length; i++) {
            var end_city = 0;
            if (tickets[start][1] == tickets[i][0]) {
                if (used.indexOf(i) == -1) {
                    if (next_check == -1) {
                        next = i;
                        next_check = i;
                    } else if (tickets[next][1] > tickets[i][1]) {
                        next = i;
                    }
                }
            }
        }
        return find_root(next, used, answer, count_len)
    }
    answer = find_root(start, used, answer, 0)
    return answer;
}