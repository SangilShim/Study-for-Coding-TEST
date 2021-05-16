# 상하좌우 문제 : 좌표위에서 명령에 따라 움직이기

# 내풀이 (정답)

n = int(input())
data = map(str,input().split())

i = 1
j = 1
for o in data:
    if o == 'R':
        if j == n:
            pass
        else:
            j += 1
    elif o == 'L':
        if j == 1:
            pass
        else:
            j -+ 1
    elif o == 'U':
        if i == 1:
            pass
        else:
            i -= 1
    elif o == 'D':
        if i == n:
            pass
        else:
            i += 1
print(i,j)

# 교재 풀이 ('이것이 코딩 테스트다','나동빈','한빛미디어',p112)
n = int(input()) 
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_tyes[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x,y = nx, ny
  
print(x,y)
