"""
 * 소요시간: 5 분
 * 시간복잡도: O(n) 	
 * 메모리: 32412 kb	
 * 시간: 36 ms
"""

import itertools

dwarf_list = []

# 9명의 난쟁이의 키 리스트 만들기
for _ in range(9):
    height = int(input())
    dwarf_list.append(height)

# 9명의 난쟁이를 7개로 조합하는 코드 생성
# 총 36개
combinations = list(itertools.combinations(dwarf_list, 7))

# 36개의 조합을 순회하면서
for comb in combinations:
    # 합이 100이면
    if sum(comb) == 100:
        # 오름차순으로 정렬하여
        comb_sorted = sorted(comb)
        # 값을 print한다
        for num in comb_sorted:
            print(num)
        break
