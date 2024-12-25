"""
 * 소요시간: 1 분
 * 시간복잡도: O(n) 	
 * 메모리: 32412 kb	
 * 시간: 44 ms
"""

# 총 숫자 갯수 - total_num
# 공백 없는 숫자 변수 - num_no_space
total_num = int(input())
num_no_space = input()
sum = 0

# 공백 없는 숫자 변수는 문자열로 받고 순회하면서
# 정수형으로 변환후 sum에 더한다
for i in range(total_num):
    sum += int(num_no_space[i])

print(sum)
