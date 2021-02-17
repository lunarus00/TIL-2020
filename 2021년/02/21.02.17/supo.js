function solution(answers) {
    var answer = [];
    var fir_supo = [];
    var sec_supo = [];
    var thi_supo = [];
    for (var i=0; i < answers.length; i++) {
        if (i%5 == 0) {
            fir_supo.push(1);
        } else if (i%5 == 1) {
            fir_supo.push(2);
        } else if (i%5 == 2) {
            fir_supo.push(3);
        } else if (i%5 == 3) {
            fir_supo.push(4);
        } else if (i%5 == 4) {
            fir_supo.push(5);
        }
        if (i%8 == 0) {
            sec_supo.push(2);
        } else if (i%8 == 1) {
            sec_supo.push(1);
        } else if (i%8 == 2) {
            sec_supo.push(2);
        } else if (i%8 == 3) {
            sec_supo.push(3);
        } else if (i%8 == 4) {
            sec_supo.push(2);
        } else if (i%8 == 5) {
            sec_supo.push(4);
        } else if (i%8 == 6) {
            sec_supo.push(2);
        } else if (i%8 == 7) {
            sec_supo.push(5);
        }
        if (i%10 == 0) {
            thi_supo.push(3);
        } else if (i%10 == 1) {
            thi_supo.push(3);
        } else if (i%10 == 2) {
            thi_supo.push(1);
        } else if (i%10 == 3) {
            thi_supo.push(1);
        } else if (i%10 == 4) {
            thi_supo.push(2);
        } else if (i%10 == 5) {
            thi_supo.push(2);
        } else if (i%10 == 6) {
            thi_supo.push(4);
        } else if (i%10 == 7) {
            thi_supo.push(4);
        } else if (i%10 == 8) {
            thi_supo.push(5);
        } else if (i%10 == 9) {
            thi_supo.push(5);
        }
    }
    var check_fir = 0;
    var check_sec = 0;
    var check_thi = 0;
    for (var i=0; i < answers.length; i++) {
        if (fir_supo[i] == answers[i]){
            check_fir++;
        }
        if (sec_supo[i] == answers[i]){
            check_sec++;
        }
        if (thi_supo[i] == answers[i]){
            check_thi++;
        }
    }
    if (check_fir >= check_sec){
        if (check_fir >= check_thi){
            answer.push(1)
        }
    }
    if (check_sec >= check_fir){
        if (check_sec >= check_thi){
            answer.push(2)
        }
    }
    if (check_thi >= check_fir){
        if (check_thi >= check_sec){
            answer.push(3)
        }
    }
    return answer;
}