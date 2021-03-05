function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    var truck_on_bridge = [];
    var truck_passed = [];
    var now_weights = 0;
    var when_truck = [];
    for (var i = 0; true; i++) {
        answer++;
        if (i == when_truck[0] + bridge_length) {
            truck_passed.push(truck_on_bridge[0]);
            now_weights -= truck_on_bridge[0]
            when_truck.shift();
            truck_on_bridge.shift();
        }
        if (now_weights < weight) {
            if (truck_weights.length > 0) {
                if (now_weights + truck_weights[0] <= weight){
                    truck_on_bridge.push(truck_weights[0]);
                    now_weights += truck_weights[0];
                    truck_weights.shift();
                    when_truck.push(i);
                }
            }
        }
        if (truck_on_bridge.length == 0) {
            break
        }
    }
    return answer;
}