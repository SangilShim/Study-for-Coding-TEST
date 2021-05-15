# 곱하기 혹은 더하기 문제 : x 혹은 + 연산자를 가지고 입력된 숫자 하나하나와 연결하여 가장 큰 수를 만드는 것이다.

# 내 풀이
# 1차 
#(출력예시 통과 13분 40초) -> 예외 : 012을 입력하면? 오류발생이다.
# i가 0 혹은 1이면 더하는 것이 유리하고, i와 num이 2 이상이라면 곱하는 게 유리하다. 

s = input()
num = 1
for i in s:
    i = int(i)
    if i == 0:
        pass
    else:
        num = num * i
if s == '0':
    num = 0
print(num)

# 2차(정답)

s = input()
num = 0
for i in s:
    i = int(i)
    num = int(num)
    if i <= 1 or num <= 1:
        num = num + i
    elif i >= 2 and num >= 2:
        num = num *  i

print(num)

# 교재풀이
data = input()
result = int(data[0])
for i in range(1,len(data)):
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num
print(result)
