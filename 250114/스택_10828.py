"""
 * 소요시간: 15 분
 * 시간복잡도: O(n) 	
 * 메모리: 33564 kb	
 * 시간: 40 ms
"""

import sys

# 입력에 시간초과가 발생해서 입력 최적화
input = sys.stdin.read
data = input().splitlines()

# 스택을 구현할 리스트 생성
stack_list = []

# 0번째 input을 전체 커맨드 갯수로 지정
command_num = int(data[0])

# 1번째 ~ 마지막 커맨드를 돌면서
for i in range(1, command_num + 1):
    command = data[i]

    # 커맨드가 top이면 맨 마지막에 있는 값 출력
    # 단, 스택에 값이 없는 경우 -1 출력
    if command == "top":
        if stack_list:
            print(stack_list[-1])
        else:
            print(-1)

    # 커맨드가 pop이면 맨 마지막에 있는 값을 스택에서 뽑아서 출력
    # 단, 스택에 값이 없는 경우 -1 출력
    elif command == "pop":
        if stack_list:
            print(stack_list.pop())
        else:
            print(-1)

    # 커맨드가 size이면 스택의 길이 출력
    elif command == "size":
        print(len(stack_list))

    # 커맨드가 empty이면 스택이 비어있는지 확인
    # 비어있으면 1 아니면 0 출력
    elif command == "empty":
        if stack_list:
            print(0)
        else:
            print(1)

    # 그 외의 상황은 push를 하는 command이므로
    # 커맨드를 'push 5' -> ('push', '5') 로 분리해야함
    # 분리한 것 중 숫자부분만 가져와서 int 처리 후 stack에 넣기
    else:
        _, num = command.split()
        stack_list.append(int(num))
