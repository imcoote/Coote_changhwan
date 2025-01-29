"""
 * 소요시간: 1 시간
 * 시간복잡도: O(n) 	
 * 메모리: 32544 kb	
 * 시간: 92 ms
"""

from collections import deque

# 입력 받기
n, w, L = map(int, input().split())
truck = deque(map(int, input().split()))

# 다리 상태를 나타내는 큐, 트럭이 없는 곳은 0으로 채우기
bridge = deque([0] * w)
time = 0


# 다음 트럭이 들어올때 무게 측정하기
# 무게를 측정해서 하중보다 큰지 작은지 체크하는 용도로 만들었음
def next_bridge_weight(next_truck):
    return sum(bridge) + next_truck - bridge[0]


# 다음 트럭 혹은 0을 스택에 추가하고 앞에 값을 빼주기
def queue(next_truck=0):
    bridge.append(next_truck)
    bridge.popleft()


# 트럭이 남아있는 동안
while truck:
    # 다음 트럭이 들어왔을 때 무게 하중보다 작으면
    if next_bridge_weight(truck[0]) <= L:
        # 가장 앞의 트럭을 빼서 다리에 추가하기
        new_truck = truck.popleft()
        queue(new_truck)
        time += 1

    # 만약 무게 하중보다 크면
    # 0을 계속 추가하기
    while truck and next_bridge_weight(truck[0]) > L:
        queue()
        time += 1


# 트럭 리스트에 더 이상 트럭이 없다면
# 모든 트럭이 지나가는 동안 시간 추가하기
while sum(bridge) > 0:
    queue()
    time += 1

# 결과 출력
print(time)
