"""
 * 소요시간: 20 분
 * 시간복잡도: O(n) 	
 * 메모리: 186660 kb	
 * 시간: 1324 ms
"""

# 좌표 갯수 N과 리스트 X에 대한 입력 받기
N = int(input())
X = list(map(int, input().split()))

# <<아이디어>>
# 좌표들을 오름차순으로 정렬한 것의 인덱스 값이 결과값이랑 같다!!

# 풀이 순서
# 1. 겹치는 좌표가 존재 할 수 있으므로 set적용
# 2. 오름차순으로 정렬한다
# 3. 좌표값을 key로 인덱스 값을 value로 하는 dict 생성 (ex: {-10: 0, -9: 1, 2: 2, 4: 3})
# 4. 원래 리스트를 돌면서 sorted_dict에서 인덱스 값을 뽑아온다

sorted_dict = {key: value for value, key in enumerate(sorted(set(X)))}

result = " ".join(str(sorted_dict[key]) for key in X)

print(result)
