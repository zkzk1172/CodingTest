#직접 데이터 넣어 초기화
a=[1,2,3,4,5]
print(a)

#3번째 원소만 출력
print(a[2])

#크기가 n이고 모든 값을 0으로 채운 리스트 초기화
n=10
a=[0]*n
print(a)

#리스트에서 거꾸로 조회하기
a=[1,2,3,4,5,6,7,8,9]
print(a[-1])
print(a[-2])
print(a[-3])

#n번째부터 m번째까지 출력
#print(a[n-1:m]) 
print(a[0:4])

#리스트 컴프리헨션
#반복문 or 조건문을 통해 리스트를 초기화
a=[i for i in range(10)]
print(a)

#조건문 추가
a=[i for i in range(10) if i%2==0]
print(a)

#제곱으로 출력
a=[i*i for i in range(10)]
print(a)

#2차원리스트에서 리스트컴프리헨션
b=[[0]*4 for _ in range(3)]
print(b)

b[1][2]=3
print(b)
