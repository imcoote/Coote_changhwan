"""
 * 소요시간: 20 분
 * 시간복잡도: O(n) 	
 * 메모리: 32544 kb	
 * 시간: 44 ms
"""

# N, A, B 입력받기
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# << 아이디어 >>

# B를 낮은 숫자순으로 번호를 매긴 리스트를 만든다 ([10, 30, 20] --> [0, 2, 1])
# 이거는 A와 B를 곱할 때 매칭시키 위한 용으로 쓰인다
# A를 내림차순으로 정렬한다.
# A를 내림차순으로 정렬하면 나중에 A와 B를 곱할때 같은 인덱스로 A의 높은 값과 B의 낮은 값을 곱할 수 있다

# N 만큼 길이의 순위 매길 리스트 생성 ([0, 1, 2, 3, ...,N])
N_range = range(N)

# 이걸 B를 값에 따라 인덱스 정렬
B_index = sorted(N_range, key=lambda x: B[x])

# A를 내림차순으로 정렬하고
A.sort(reverse=True)

# B의 인덱스 가져와서 내림차순으로 정렬한 A와 곱하기
result = sum(A[i] * B[B_index[i]] for i in range(N))
print(result)
