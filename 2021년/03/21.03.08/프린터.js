function solution(priorities, location) {
    var answer = 0;
    var check_priority = 0;
    var flag = 0;
    var paper_list = new Array(priorities.length);
    paper_list[location] = 'A';
    var check_paper = '';
    for (var i = 0; priorities.length > 0;) {
        flag = 0;
        check_priority = priorities[0];
        check_paper = paper_list[0];
        priorities.shift();
        paper_list.shift();
        location--;
        for (var j = 0; j < priorities.length; j++) {
            if (priorities[j] > check_priority) {
                priorities.push(check_priority);
                paper_list.push(check_paper);
                flag = 1;
                break
            }
        }
        if (flag == 0) {
            answer++;
            if (check_paper == 'A') {
                break
            }
        }
    }
    return answer;
}