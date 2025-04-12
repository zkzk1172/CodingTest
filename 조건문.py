# 조건문
n = int(input("정수를 입력하세요: "))

if n % 2 == 0:
  print(f"{n}은 짝수")
elif n % 2 == 1:
  print(f"{n}은 홀수")
else:
  pass # 아무것도 하지 않음, 잠깐 비워두고 싶을 때 pass 사용


# 기타 연산자

# x in 리스트 -> 리스트 안에 x가 있으면 True
# x not in 문자열 -> 문자열 안에 x가 없으면 True

# 조건부 표현식은 if-else를 한 줄에 작성할 수 있게 해줌
score=int(input())
grade='A' if score >=95 else 'B'
print(grade)
