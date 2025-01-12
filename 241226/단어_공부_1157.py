"""
 * 소요시간: 10 분
 * 시간복잡도: O(n) 	
 * 메모리: 43208 kb	
 * 시간: 128 ms
"""

from collections import Counter

# 문자열 입력 받기
word = input()

# 받은 문자열을 대문자 처리 후
# 각 문자를 담은 리스트 생성, 그리고 Counter 클래스로 숫자세기
word_count = Counter(list(word.upper()))

# Counter에서 가장 빈도수 높은 것을 구하는 메서드 most_common 사용
# [('I', 4), ('S', 4)]
if len(word_count) > 1:
    most_common = word_count.most_common(2)

    if most_common[0][1] == most_common[1][1]:
        print("?")
    else:
        print(most_common[0][0])
# 알파벳이 하나로만 구성되있을 경우 길이가 1이다
# [('A', 4)]
else:
    most_common = word_count.most_common(1)

    print(most_common[0][0])
