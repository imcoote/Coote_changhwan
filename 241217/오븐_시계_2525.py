"""
 * 소요시간: 10 분
 * 시간복잡도: O(n) 	
 * 메모리: 32412 kb	
 * 시간: 32 ms
"""

# 현재 시, 분, 그리고 조리시간 입력받기
now_hour, now_minute = map(int, input().split())
cooking_minute = int(input())

# 계산을 위해 분단위로 현재 시각에서 조리시간을 더 하기
target_minute = now_hour * 60 + now_minute + cooking_minute

# 60으로 나눈 몫이 hour, 나머지가 minute
hour = target_minute // 60
minute = target_minute % 60

# 24시가 넘었을 경우 24를 빼주기
print(hour if hour < 24 else hour - 24, minute)
