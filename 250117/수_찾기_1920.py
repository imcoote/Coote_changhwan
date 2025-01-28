"""
* 첫번째 풀이
    * 소요시간: 5 분
    * 시간복잡도: O(n) 	
    ! 시간초과

* 두번째 풀이
    * 소요시간: 5분
    * 시간복잡도: O(1)
    * 메모리: 50680 kb	
    * 시간: 148 ms

* 세번째 풀이
    * 소요시간: 20분
    * 시간복잡도: O(logn)
    * 메모리: 48600 kb	
    * 시간: 452 ms
"""

# <<첫번째 풀이 - 시간초과!!>>

# 마지막 배열을 순회하면서 A안에 있는 지 확인하는 방식으로 풀려고 했습니다만
# 시간초과가 났습니다...
N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

for value in B:
    print(1 if value in A else 0)


# <<두번째 풀이 - set 사용>>

# 구글링 해보니 in 연산자를 효율적으로 사용하려면 집합으로 변환시켜야 한다고 하더라구요!
# set 자료구조에서 in 연산자를 사용하는것은 무려 **O(1)**의 시간복잡도를 가진다는 사실..
# 그래서 변환해서 사용하니까
# 50680kb 메모리 사용량과 148ms의 시간이 걸렸습니다
N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

set_A = set(A)

for value in B:
    print(1 if value in set_A else 0)


# <<세번째 풀이 - 이진탐색 사용>>

# 질문게시판을 보니까 이진탐색을 사용해서 푼 사람이 많더라구요?
# 그래서 저도 이진탐색으로 풀어봤습니다!
# 일단 이진탐색을 하기전 A 배열을 정렬 시켰습니다
# 결과는 메모리 48600kb, 시간은 452ms가 나왔습니다
# 시간은 set를 사용한것 보다 더 걸렸지만 메모리는 적게 사용한 결과가 나왔습니다!
N = int(input())
A = sorted(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))


def binary_search(list, target):
    left, right = 0, len(list) - 1

    while left <= right:
        mid = (left + right) // 2

        if list[mid] == target:
            return True
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


for value in B:
    print(1 if binary_search(A, value) else 0)
