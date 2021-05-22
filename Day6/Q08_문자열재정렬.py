# Q08. 문자열 재정렬 문제. 알파벳과 숫자가 입력되면 오름차순으로 정렬하여 이어붙여라.
# 알아갈 함수: ''.join(리스트)    ,   변수.isalpha()

# 내 풀이 (정답) : 리스트를 문자열로 바꾸는 함수 -> ''.join() 암기하자!
n = input()
number= ['0','1','2','3','4','5','6','7','8','9']
num = 0
string = []

for i in n:
    if i in number:
        i = int(i)
        num += i
    else:
        string.append(i)

num = str(num)
string.sort()

print(''.join(string) + num)

# 교재풀이 ('이것이 코딩테스트다',나동빈,한솔미디어,p516)
# 변수.isalpha()라는 함수를 통해 문자 혹은 숫자와의 비교하는 과정을 줄일 수 있다.
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()
if value != 0:
    result.append(str(value))

print(''.join(result))
