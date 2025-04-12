# 함수
# def 함수명(매개변수):
#     실행코드
#     return 반환값

def add(a,b):
  return a+b

print(add(3,4))

# global 키워드 -> 전역변수 = 함수 외부의 변수

a=0

def func():
  global a
  a+=1

for i in range(10):
  func()

print(a)

# 람다함수 -> lambda 매개변수 : 표현식
# 내장함수에서 자주 사용

arr = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]

def my_key(x):
  return x[1]

print(sorted(arr, key=my_key)) # 함수 사용
print(sorted(arr, key=lambda x:x[1],reverse=True)) # 람다식 사용

# 여러 리스트에 적용되는 람다식

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

result = map(lambda a,b: a+b,list1,list2)
print(result) # 람다식을 거친 데이터들은 map객체에 저장됨 = map객체라는 메모리 주소상에 저장된다는것
list3=list(result)
print(list3)
