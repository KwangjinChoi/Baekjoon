def my_answer():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split(' '))
        com = ((a%10)**b)%10
        if com == 0:
            com = 10

        print(com)
    # 시간 초과...

# input으로 받으면 시간 초과가 날 수 있다.
# sys.stdin.readline()을 이용하면 빠름 (반복문에서 받을 때)
T = int(input())
answer = [[10],[1], [2,4,8,6], [3,9,7,1], [4,6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
for _ in range(T):
    a, b = map(int, input().split(' '))
    a = a%10
    b = b%len(answer[a])
    print(answer[a][b-1])
