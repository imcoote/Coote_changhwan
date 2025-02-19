"""
 * 소요시간: 3 시간
 * 시간복잡도: O(n) 	
 * 메모리: 32544 kb	
 * 시간: 40 ms
"""

# 돌 숫자 입력 받기
N = int(input())

# << 아이디어 >>

# 처음에는 '완벽한 게임'이 뭔지부터 이해가 안되서 많이 헤매다가
# 구글링과 gpt한테 완벽한 게임이 뭐냐고 물어서 몇가지 힌트를 얻고 진행하였습니다

# '완벽한 게임'은 게임이 시작되기 전에 양쪽이 완벽한 전략을 사용할 경우 승패는 이미 정해져 있다고 합니다..
# 돌 게임에서는 돌의 개수(N)에 따라 승패가 결정된다고 해서
# 저는 돌의 개수에서 힌트를 얻기 위해서 돌이 1개일때 부터 누가 이기는지 다 체크해봤습니다..

# 돌이 1개: 상근이가 가져가서 승리 → '무조건' 이기는 상태
# 돌이 2개: 창영이가 가져가서 승리 → '무조건' 지는 상태
# 돌이 3개: [처음 상근이의 선택에따라 승패가 다름]
# 돌이 4개: [처음 상근이의 선택에따라 승패가 다름]
# 돌이 5개: [처음 상근이의 선택에따라 승패가 다름]
# 돌이 6개: [처음 상근이의 선택에따라 승패가 다름]
# 돌이 7개: 상근이가 어떤 선택을 하더라도 창영이가 반드시 승리 → '무조건' 지는 상태

# 이 때 상근이의 선택에 따라 승패가 다르게 나온 지점들은 무조건 상근이가 승리한다고 판단했습니다
# 왜냐하면 '상근'이가 먼저 시작하고 상근이가 최선의 판단을 내린다고 가정 했습니다

# 쭉 체크를 해보면 돌이 2개 혹은 7개인 지점에서 무조건 지는 상태가 나옵니다

# 그래서 이게 돌 갯수를 7로 나누었을 때 2나 0으로 나머지가 나오는 돌 갯수가 무조건 지는 지점이 아닐까..?
# 그렇게 생각해서 해봤더니 통과가 되었습니다....
# 정확한 수학적인 해석을 바탕으로 푼게 아니라서 좀 찝찝하긴 한데 풀긴 풀었네요..


# 7로 나누어 떨어지거나 2가 남는다면
# 어떤 짓을 해도 못이기기 때문에 창영이가 승리
# 아니면 상근이의 승리
if N % 7 == 0 or N % 7 == 2:
    print("CY")
else:
    print("SK")

# 이상으로 코드보다 주석이 더 긴 풀이였습니다...
