a=[1,3,4,2,5]

#리스트에 원소삽입
a.append(6)
print(a)

#리스트 오름차순 정렬
a.sort()
print(a)

#리스트 내림차순 정렬
a.sort(reverse=True)
print(a)

#리스트 뒤집기
a.reverse()
print(a)

#특정 인덱스에 원소 추가
a.insert(2,3)
print(a)

#특정 값의 원소 개수
print(a.count(3))

#특정 값 제거
a.remove(5)
print(a)

#리스트에서 특정값을 가지는 원소 모두 제거
a=[1,2,3,4,5,5,5]
remove_set={1,5}

result = [i for i in a if i not in remove_set]
print(result)
