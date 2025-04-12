# 반복문
# for문 -> for 변수 in list: 실행할 코드

arr = list(map(int, input().split()))
result =[]

for i in arr:
  if i % 2 == 0:
    result.append(i)

print(result)

# continue -> continue를 만나면 다음 코드를 실행하지 않고 다음 반복으로 넘어감
# continue 사용해서 홀수의 합 구하기

ans = 0
for i in range(1,11):
  if i%2==0:
    continue
  ans += i

print(ans)
