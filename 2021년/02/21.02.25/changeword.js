function solution(begin, target, words) {
    var answer = 0;
    var visit_word = [];
    function find_target(id, target, words, word, answer, visit_word) {
        if (word == target) {
            return answer
        } else if (id == words.length - 1) {
            return answer
        }
        for (var i = 0; i < words.length; i++) {
            if (visit_word.indexOf(words[i]) == -1) {
                var check_word = 0;
                for (var j = 0; j < words[i].length; j++) {
                    if (word[j] == words[i][j]) {
                        check_word++;
                    }
                }
                if (check_word == target.length) {
                    return answer
                } else if (check_word == target.length - 1) {
                    visit_word.push(words[i])
                    answer = find_target(i + 1, target, words, words[i], answer + 1, visit_word);
                    return answer
                }
            }
        }
        return answer
    }
    if (words.indexOf(target) != -1) {
        for (var k = 0; k < words.length; k++){
            var check_word = 0;
            for (var l = 0; l < words[k].length; l++) {
                if (begin[l] == words[k][l]) {
                    check_word++;
                }
            }
            if (check_word == target.length) {
                answer = 0;
            } else if (check_word == target.length - 1) {
                visit_word.push(words[k])
                answer = find_target(k+1, target, words, words[k], answer+1, visit_word)
            }
        }
    }
    return answer;
}