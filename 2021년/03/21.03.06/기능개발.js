function solution(progresses, speeds) {
    var answer = [];
    for (var i = 0; progresses.length > 0; i++) {
        if (progresses[0] >= 100) {
            var check_program = 0;
            for (var j = 0; true;) {
                if (progresses[0] >= 100) {
                    progresses.shift();
                    speeds.shift();
                    check_program++;
                } else {
                    break
                }
            }
            answer.push(check_program);
        }
        for (var j = 0; j < progresses.length; j++) {
            progresses[j] += speeds[j]
        }
    }
    return answer;
}