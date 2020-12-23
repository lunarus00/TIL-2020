"""
8자리의 숫자 입력
날짜가 유효한 경우 YYYY/MM/DD 형식으로 출력
그렇지 않은 경우 -1을 출력
윤년은 미고려, 2월은 28일까지
"""

T = int(input())
for tc in range(T):
    str_date = input()
    year_date = str_date[0:4]
    month_date = str_date[4:6]
    day_date = str_date[6:8]
    if int(month_date) > 12 or int(month_date) == 0:
        print(f'#{tc+1} -1')
    elif int(month_date) == 2:
        if int(day_date) > 28:
            print(f'#{tc+1} -1')
        else:
            print(f'#{tc+1} {year_date}/{month_date}/{day_date}')
    elif int(month_date) > 7:
        if int(month_date) % 2 == 0:
            if int(day_date) > 31:
                print(f'#{tc+1} -1')
            else:
                print(f'#{tc+1} {year_date}/{month_date}/{day_date}')
        else:
            if int(day_date) > 30:
                print(f'#{tc+1} -1')
            else:
                print(f'#{tc+1} {year_date}/{month_date}/{day_date}')
    elif int(month_date) <= 7:
        if int(month_date) %2 != 0:
            if int(day_date) > 30:
                print(f'#{tc+1} -1')
            else:
                print(f'#{tc+1} {year_date}/{month_date}/{day_date}')
        else:
            if int(day_date) > 31:
                print(f'#{tc+1} -1')
            else:
                print(f'#{tc+1} {year_date}/{month_date}/{day_date}')
    else:
        print(f'#{tc+1} {year_date}/{month_date}/{day_date}')