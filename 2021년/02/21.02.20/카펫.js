function solution(brown, yellow) {
    var answer = [];
    // 가로 세로 둘 다 3칸 이상은 되어야 함
    // 테두리의 크기를 구하는 방법을 먼저 만든다
    for (var i = 3; i < brown/2; i++){
        if ((brown-i*2)%2 == 0){
            var height = (brown-i*2)/2+2
            if (i >= height) {
                if (i * height - brown == yellow){
                    answer.push(i)
                    answer.push(height)
                }
            }
        }
    }
    return answer;
}