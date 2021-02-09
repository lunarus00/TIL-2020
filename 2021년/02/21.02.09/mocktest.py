def solution(answers):
    problems = len(answers)
    answer = []
    fir_person = []
    sec_person = []
    thi_person = []
    for i in range(1, problems+1):
        if i % 5 == 1:
            fir_person.append(1)
        elif i % 5 == 2:
            fir_person.append(2)
        elif i % 5 == 3:
            fir_person.append(3)
        elif i % 5 == 4:
            fir_person.append(4)
        else:
            fir_person.append(5)
        if i % 8 == 1:
            sec_person.append(2)
        elif i % 8 == 2:
            sec_person.append(1)
        elif i % 8 == 3:
            sec_person.append(2)
        elif i % 8 == 4:
            sec_person.append(3)
        elif i % 8 == 5:
            sec_person.append(2)
        elif i % 8 == 6:
            sec_person.append(4)
        elif i % 8 == 7:
            sec_person.append(2)
        else:
            sec_person.append(5)
        if i % 10 == 1 or i % 10 == 2:
            thi_person.append(3)
        elif i % 10 == 3 or i % 10 == 4:
            thi_person.append(1)
        elif i % 10 == 5 or i % 10 == 6:
            thi_person.append(2)
        elif i % 10 == 7 or i % 10 == 8:
            thi_person.append(4)
        else:
            thi_person.append(5)
    check_fir = 0
    check_sec = 0
    check_thi = 0
    for i in range(problems):
        if answers[i] == fir_person[i]:
            check_fir += 1
        if answers[i] == sec_person[i]:
            check_sec += 1
        if answers[i] == thi_person[i]:
            check_thi += 1
    if check_fir >= check_sec and check_fir >= check_thi:
        answer.append(1)
    if check_sec >= check_fir and check_sec >= check_thi:
        answer.append(2)
    if check_thi >= check_fir and check_thi >= check_sec:
        answer.append(3)
    return answer