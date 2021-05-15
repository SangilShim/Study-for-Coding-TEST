# 문자열 뒤집기 - 0과 1로 이루어진 문자열을 모두 0으로 혹은 1로 바꿀 때 더 적은 횟수로 만들기

# 내 풀이 (오답)
# 0으로 뒤집는 경우와 1로 뒤집는 경우 모두를 생각하지 못했다. 그 다음 숫자랑 비교하는 방법에 대해 생각해보지 못했다.
s = input()
count = 0
sum = s[0]
for i in s:
    i = int(i)
    if sum == 0 and i == 0:
        pass
    elif sum == 0 and i == 1:
        sum = 1
    elif sum == 1 and i == 0:
        count += 1
        sum = 0
    elif sum == 1 and i ==1:
        sum = 1
print(count) 

# 교재풀이 ('이것이 코딩테스트다' , 나동빈, 한빛미디어, p509)
# 0으로 바꾸는 횟수와 1로 바꾸는 횟수를 따로 카운팅해서 그 중에 작은 수를 greedy에 맞게 선택했다. data[i] 와 data[i+1]을 사용하여 비교하는 것이 흥미롭다
data = input()

count0 = 0 # 0으로 바꾸는 횟수
count1 = 0 # 1로 바꾸는 횟수

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0,count1))
