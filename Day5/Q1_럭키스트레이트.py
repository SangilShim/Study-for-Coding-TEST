# Q1 럭키 스트레이트 문제 - 짝수의 정수가 입력되면 절반을 기준으로 슬라이싱 했을 때 각 자릿수의 합이 양쪽이 같다면 럭키를 아니면 레디를 출력해내는 문제.

# 내 풀이 : 정답 (15분)  -> range 함수를 이용해서 구현해보려고 했는데, 아직 개념이 많이 부족한 것 같았다. 그래서 문자열로 바꾼 후 슬라이싱을 해서 풀었다. 
# 끝을 len(n)/2 로 설정했더니 slice indices must be integers or None or have an __index__ method 라고 나왔었다.
# 몫이라는 확실한 명령을 해야 하는 것 같다.


n = int(input())
n = str(n)
sum_front = 0
sum_back = 0

front = n[0:(len(n)//2)]
back = n[(len(n)//2):]

for i in front:
    i = int(i)
    sum_front += i
for j in back:
    j = int(j)
    sum_back += j

if sum_front == sum_back:
    print("LUCKY")
else:
    print("READY")
    
# 교재 풀이 ('이것이 코딩테스트다', 나동빈, 한솔미디어, p515)
# 내가 처음 원했던 RANGE 함수를 이용하여 구현해내었다. 입력 값도 정수라고 해서 나는 STRING으로 변환을 했었는데, 해설에서는 애초에 문자열로 입력하였다. 
# SUM이 결국 0이 되도록 성립되게 만든 아이디어가 돋보인다.

n = input()
length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length//2,length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")
