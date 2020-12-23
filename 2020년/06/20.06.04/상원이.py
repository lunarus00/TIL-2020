import sys, time

start = time.time()

sys.stdin = open('상원이.txt')

T = int(input())

def find_friends(person):
    global invite_friend
    for i in range(N):
        if friend_list[person][i] == 1:     # 권한을 가진 person 과 친한 관계인지 확인
            if visited[i] == 0:             # 아직 초대되지 않은 경우
                visited[i] = 1              # 초대 표시를 하고
                invite_friend += 1          # 초대 인원 수를 늘린 후
                if person == 1:             # 1(상원이)의 베프인 경우에만
                    invite_list.append(i)   # 초대장 발송 권한을 부여

for tc in range(T):
    N, M = list(map(int, input().split()))
    friend_list = [[0] * (N+1) for i in range(N+1)]
    for i in range(M):
        num_one, num_two = list(map(int, input().split()))
        friend_list[num_one][num_two] = 1 # 친한 관계 입력받아 표시
        friend_list[num_two][num_one] = 1
    visited = [0] * (N+1)   # 이미 초대된 친구인지 표시
    invite_list = [1]       # 초대장 발송 권한
    visited[1] = 1          # 1(상원이) 초대받지 않도록 표시
    invite_friend = 0       # 초대받은 인원 수 확인
    while len(invite_list) > 0:         # 초대장 발송 권한이 있는 아이가 남아있으면 반복
        find_friends(invite_list[0])    # 초대 확인 함수
        invite_list.pop(0)              # 초대장 발송한 아이의 권한을 삭제
    print('#{} {}'.format(tc+1, invite_friend))

print(time.time() - start)