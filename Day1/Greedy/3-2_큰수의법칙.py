# 그리디_실전문제_1. 큰수의 법칙 
# 복습할 내용) (5/15) 책에서는 while True: 를 for문 앞에 붙여줬는데 이거를 붙이지 않으면 어떤 오류가 생기는지

# n = 입력될 자연수의 수, m = 숫자가 더해지는 횟수, k = 최대 더해질 수 있는 횟수
n,m,k = map(int,input().split())
# 자연수 n개가 주어진다. 가장 큰 수를 최대한 많이 더할수록 큰 수가 나올 것이니 큰 수부터 찾자.
data = list(map(int,input().split()))
data.sort()
first_max = data[-1]
# 가장 큰 수를 연속해서 더할 수 있는 횟수가 숫자가 더해지는 횟수보다 작다는 전제가 있으므로 두번째 큰 수도 찾자.
second_max = data[-2]

# 첫번째 큰 숫자를 k번 만큼 더해주는 반복문과, 두번째 숫자를 k번 만큼 더해주는 반복문을 만든다.
sum = 0
for i in range(k):
    if m == 0:
        break
    else:
        sum += first_max
        m -= 1
for j in range(k):
    if m == 0:
        break
    else:
        sum += second_max
        m -= 1

print(sum)
