function solution(input_numbers) {
    var answer = 0;
    var check_list = [];
    for (var i = 0; i < input_numbers.length; i++) {
        check_list.push(input_numbers[i]);
    }
    function getNumbeOfCases(numbers) {
        // 중복을 막기 위해서
        const result = new Set();

        // 재귀 함수를 통해 만든다.
        const temp = (currFix, eachArr) => {
            for (let i = 0; i < eachArr.length; i++) {
                const tempEachArr = [...eachArr];
                const tempCurrFixVal = tempEachArr.splice(i, 1)[0];
                const tempCurrFix = currFix + tempCurrFixVal;
                result.add(Number(tempCurrFix));
                if (tempEachArr.length > 0) temp(tempCurrFix, tempEachArr);
            }
        };

        // 시작
        for (let i = 0; i < numbers.length; i++) {
            let target = numbers[i];
            result.add(Number(target));

            const eachArr = [...numbers];
            eachArr.splice(i, 1);

            temp(target, eachArr);
        }

        return new Array(...result);
    }
    var num_list = getNumbeOfCases(check_list);
    for (var i = 0; i < num_list.length; i++){
        if ((num_list[i]*1) == 0){
            num_list.splice(i, 1);
            i--;
        } else if((num_list[i]*1) == 1){
            num_list.splice(i, 1);
            i--;
        }
    }
    // console.log(check_list)
    // console.log(num_list)
    for (var i = 0; i < num_list.length; i++){
        if (num_list[i] == 2){
            answer++;
        }
        for (var j = 2; j < num_list[i]-1; j++){
            if (num_list[i] % j == 0){
                break;
            } else if (j == num_list[i] - 2) {
                answer++;
            }
        }
    }
    return answer;
}