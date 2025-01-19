"""
 * 소요시간: 10 분
 * 시간복잡도: O(n) 	
 * 메모리: 32412 kb	
 * 시간: 36 ms
"""

num_list = []

# 9 * 9 행렬 생성
for i in range(9):
    num_list.append(list(map(int, input().split())))

max_num = 0
max_coor = (1, 1)

# 9 * 9 이중 배열을 돌면서
# 최댓값 확인
for m in range(9):
    for n in range(9):
        if num_list[m][n] > max_num:
            max_num = num_list[m][n]
            max_coor = (m + 1, n + 1)

print(max_num)
print(max_coor[0], max_coor[1])
