# 잔돈이 1730원이라고 가정했을 때, 가장 적은 수의 잔돈을 주려면 어떻게 해야 할까?
# 복습할 내용 : (5/15) 잔돈이 서로 배수가 아니라면 어떤 알고리즘을 사용해야 하는가? -> 다이나믹 프로그래밍
#              (5/15)  '%=' 연산자의 의미는? -> '%=' 연산자는 왼쪽 변수에서 오른쪽 값을 나눈 나머지의 결과를 왼쪽 변수에 할당한다.
n = 1730
count = 0
# 다행히 잔돈이 서로 배수이므로 그리디 유형의 문제이다.
coin_type = [500, 100, 50, 10]


for i in coin_type:
    count += n // i
    n %= i

print(count)
