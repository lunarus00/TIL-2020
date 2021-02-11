def solution(brown, yellow):
    answer = []
    # 가로 세로 둘 다 3칸 이상은 되어야 함
    # 테두리의 크기를 구하는 방법을 먼저 만든다
    for i in range(3, brown//2):
        check = brown - i * 2
        if check % 2 == 0:
            if i * (check / 2 + 2) - brown == yellow:
                if i >= check / 2 + 2:
                    answer = [i, check / 2 + 2]
                    break
    return answer