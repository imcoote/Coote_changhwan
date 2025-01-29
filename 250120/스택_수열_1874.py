"""
 * 소요시간: 1 시간
 * 시간복잡도: O(n) 	
 * 메모리: 39268 kb	
 * 시간: 2596 ms
"""

# n -> 입력받을 수열 길이
# sequence -> 수열
n = int(input())
sequence = [int(input()) for _ in range(n)]

# 스택은 숫자를 빼내고 넣을 공간을 위한 리스트
# result는 '+'와 '-'를 넣어 결과값을 출력하기 위한 리스트
# current는 숫자 입력 체크를 위한 숫자
# is_possible은 가능한지 불가능한지 체크하기 위한 플래그
stack = []
result = []
current = 1
is_possible = True

# << 전체적인 아이디어 >>

# 수열에 있는 숫자만큼 계속 push해주며 결과값에는 '+'를 넣어주고
# 수열에 있는 숫자에 도달하면 pop을 해준다
# 이 때 뒤로 되돌아간 경우에 다시 앞으로 나아갈 때 시작점을 알 수 있도록 해주기 위해
# 값(current)을 하나 만들면 되지 않을까..?

# 수열을 순회하며
for num in sequence:
    # 현재 숫자(current)가 수열에 있는 숫자(num)보다 작거나 같으면 push 연산을 수행
    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1

    # 스택에 숫자가 있고 마지막 숫자과 현재 수열에 있는 숫자(num)과 같아지면
    # 스택에서 pop을 하고 '-'를 결과값에 넣기
    # 그것이 실행 되지 않는 다면 is_possible은 False
    if stack and stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        is_possible = False
        break

# 출력이 가능하면 출력값 내놓고 아니면 NO 출력
if is_possible:
    print("\n".join(result))
else:
    print("NO")
