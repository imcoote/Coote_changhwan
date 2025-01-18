"""
 * 소요시간: 5 분
 * 시간복잡도: O(n) 	
 * 메모리: 32412 kb	
 * 시간: 36 ms
"""

# 자연수 두개 입력 받기
M = int(input())
N = int(input())

# 완전 제곱수 담을 리스트 생성
perfect_square = []

# 두 자연수 사이를 순회하며
for i in range(M, N + 1):
    # 루트를 씌운 값이 정수 인지 체크 한후
    # 정수이면 완전 제곱수
    if i**0.5 == int(i**0.5):
        perfect_square.append(i)

# 만약 완전 제곱수가 없다면 -1 출력
# 있다면 첫번째 줄에 합친 값과 2번째 줄에 최솟값 출력
if len(perfect_square) == 0:
    print(-1)
else:
    print(sum(perfect_square))
    print(min(perfect_square))
