#데이터 개수 입력받기
n = int(input())

#입력한 데이터 개수많큼 데이터 입력하기, 단 구분은 공백으로
data = list(map(int, input().split()))
#map함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
#map(적용할 함수, 함수에 적용할 값들)-> map(int, input().split())-> map객체 반환)
#여기서 map객체는 split()으로 입력받은 값을 int로 변환해주는 역할을 함

print(sorted(data))

#print: f-string

answer = 7
print(f"답은 {answer}입니다.")
