function solution(n, computers) {
    var answer = 0;
    var visited = new Array(n);
    visited.fill(0);
    function find_network(n, computers, visited, num) {
        var check_que = [];
        visited[num] = 1;
        check_que.push(num);
        for (var j = 0; j < check_que.length; j++) {
            for (var k = 0; k < n; k++) {
                if (computers[check_que[j]][k] == 1) {
                    if (check_que.indexOf(k) == -1) {
                        visited[k] = 1;
                        check_que.push(k);
                    }
                }
            }
        }
        return visited
    }
    for (var i = 0; i < n; i++) {
        if (visited[i] == 0) {
            answer++;
            visited = find_network(n, computers, visited, i);
        }
    }
    return answer;
}