#사전자료형 = key와 value의 쌍으로 이루어진 자료형, 변수값 변경불가
data=dict()

data['장연']='0322'
data['지은']='0623'
data['동수']='0811'

print(data)

if '장연' in data:
  print("장연님의 생일은" + data['장연'] +"입니다.")


#key나 value만 리스트로 묶을 수 있음

key_list = data.keys()
value_list = data.values()

print(key_list)
print(value_list)

#집합 자료형 초기화 = 중복이 없고 순서가 없음,특정원소 조회할때 유용
a=set([1,1,2,2,3,3,4,4,5,5])
print(a)

#새로운 원소 추가
a.add(6)
print(a)

#새로운 원소 여러개 추가
a.update([7,8,9])
print(a)

#특정 값 삭제
a.remove(3)
print(a)
