"""
 * 소요시간: 30 분
 * 시간복잡도: O(n)
 * 메모리: 34908 kb	
 * 시간: 60 ms
"""

from collections import Counter

# input()을 통해 값들을 입력받고 map 함수로 전체 배열 문자열 -> 정수화 처리
# 리스트 함수로 리스트로 만들기
# 카운터 함수로 각 숫자가 얼마나 있는지 세기
dice_list = list(map(int, input().split()))
dice_dict = Counter(dice_list)

# 가장 빈도수가 높은 숫자 구하기
max_key = max(dice_dict, key=dice_dict.get)

# 빈도수에 따른 상금 결정하기
if dice_dict[max_key] == 3:
    prize = 10000 + max_key * 1000
elif dice_dict[max_key] == 2:
    prize = 1000 + max_key * 100
elif dice_dict[max_key] == 1:
    prize = max(dice_list) * 100

print(prize)
