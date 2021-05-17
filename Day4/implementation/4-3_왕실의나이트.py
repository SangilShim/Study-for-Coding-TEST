# 왕실의 나이트 문제 : 좌표를 입력하면 체스판에서 나이트가 움직일 수 있는 방법의 최댓값 구하기
# 내풀이 (정답) : 풀이는 길지만 논리는 맞다. 교재 참고해서 더 간단한 방법을 알아내야겠다. 0=[
n = input()
data = ['R', 'L', 'U', 'D']
x = n[0] 
x = ord(x)
y = int(n[1])

count = 0

for i in data:
    if i == 'R':
        if x >= ord('g'):
            pass
        else:
            if y <= 2 or y >= 7:
                count += 1
            else:
                count += 2
    elif i == 'L':
        if x <= ord('b'):
            pass
        else:
            if y >= 7 or y <= 2:
                count += 1
            else:
                count += 2
    elif i == 'U':
        if y <= 2:
            pass
        else:
            if x <= ord('b') or x >= ord('g'):
                count += 1
            else:
                count += 2
    else:
        if y >= 7:
            pass
        else:
            if x <= ord('b') or x >= ord('g'):
                count += 1
            else:
                count += 2

print(count)

# 교재 풀이 ('이것이코딩테스트다', 나동빈, p117)
point = input()
row = int(point[1])
column = int(ord(point[0]) - int(ord('a')) + 1 # 이렇게 ord한 숫자에서 a의 ord 값을 빼주면 row 처럼 정수로 표현 가능해진다.
             
# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2,-1), (-1,-2), (2,-1), (1,-2), (2,1), (1,2), (-1,2), (-2,1)]

result = 0
for step in steps:
             next_row = row + step[0]
             next_column = column + step[1]
             if next_row >= 1 and next_row <= 8 and next_cloumn >= 1 and next_column <= 8:
                result += 1
 print(result)
