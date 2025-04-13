# x좌표가 증가하는 순서 = 오름차순 1,2,3..
# x좌표가 같을 땐 y좌표가 오름차순

n = int(input())
ls =[]

for _ in range(n):
  a,b = map(int, input().split())
  ls.append((a,b))

ls = sorted(ls, key = lambda x : (x[0], x[1]))

for x in ls:
  print(' '.join(map(str,x)))
