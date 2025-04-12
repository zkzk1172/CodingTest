# 실전에서 유용한 표준 라이브러리

# 내장함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수 제공
# sum(), min(), max(), eval(), sorted() 등
result = sum([1, 2, 3, 4, 5])
result = min(7, 3, 5, 2)
result = max(7, 3, 5, 2)
result = eval("(3+5)*7")
result = sorted([9, 1, 8, 5, 4])
arr = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(arr, key=lambda x: x[1], reverse=True)

# itertools : 파이썬의 반복되는 데이터 처리를 위한 유용한 기능 -> 순열,조합 ..
from itertools import permutations, combinations, product, combinations_with_replacement
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # ABC,ACB,BAC,BCA,CAB,CBA
result = list(combinations(data, 2)) # AB,AC,BC

# heapq : 힙(Heap) 자료구조 제공

# bisect : 이진 탐색 기능 제공

# collections : 덱(deque), 카운터(Counter) 등 유용한 자료구조 포함
#Counter : 등장 횟수를 세는 기능
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # 'blue'가 등장한 횟수 출력

# math : 필수적인 수학적 기능 제공
# 최대공약수와 최소공배수
import math
a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수
print(math.lcm(21, 14)) # 최소 공배수

