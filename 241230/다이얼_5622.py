"""
 * 소요시간: 3 분
 * 시간복잡도: O(n) 	
 * 메모리: 32412 kb	
 * 시간: 32 ms
"""

# 알파벳 별로 걸리는 시간 매핑
dial_dict = {
    "A": 3,
    "B": 3,
    "C": 3,
    "D": 4,
    "E": 4,
    "F": 4,
    "G": 5,
    "H": 5,
    "I": 5,
    "J": 6,
    "K": 6,
    "L": 6,
    "M": 7,
    "N": 7,
    "O": 7,
    "P": 8,
    "Q": 8,
    "R": 8,
    "S": 8,
    "T": 9,
    "U": 9,
    "V": 9,
    "W": 10,
    "X": 10,
    "Y": 10,
    "Z": 10,
}

dial_str = input()
dial_time = 0

# 문자열을 돌면서 해당 문자의 다이얼 시간 더하기
for char in dial_str:
    dial_time += dial_dict[char]

print(dial_time)
