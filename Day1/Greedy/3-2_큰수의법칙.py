# 그리디_실전문제_1. 큰수의 법칙 

# 복습할 내용) (5/15) 교재에서는 while True: 를 for문 앞에 붙여줬는데 이거를 붙이지 않으면 어떤 오류가 생기는지 -> 내림차순으로 계속 이어나갔을 것이다. 그러면 가장 greedy한 값이 나오지 않는다.
#                    내가 푼 두번째 풀이와는 다르게 책에서는 반복되는 수열을 파악한 후, 그 수열의 길이를 구하여 더해지는 횟수에서 이를 나눈 몫을 수열이 반복되는 횟수라고 가정한다.
#                    여기에 가장 큰 수를 곱해주면 가장 큰 값이 나오게 되는데, 나누어 떨어지지 않는 경우에는 나머지만큼 가장 큰 수가 추가로 더해진다고 가정한다. count = 몫 + 나머지
#                    m에서 count를 뺀 값에는 두번째 큰 수를 곱해주었다.
#             (5/15) 정렬 값의 가장 큰수가 리스트에서 마지막 수이므로 data[-1]이라고 했는데, 교재에서는 data[n-1]이라고 했다. 인덱스 번호 그대로 한 것 같은데, 나처럼 해도 예외가 안생기나 

 

# 첫번째 풀이 (오답)

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
# 이렇게 하면 답이 33이 나온다. 왜냐하면 가장 큰 수를 최대 횟수 만큼 더한 후, 두번째로 큰 수를 최대 횟수만큼 더하는 값보다는 
# 두번째 수는 한번만 더하고 다시 가장 큰 수를 반복하는 편이 더 greedy하기 때문이다.

# 두번째 풀이 (정답)

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
while True:
    for i in range(k):
        if m == 0:
            break
        else:
            sum += first_max
            m -= 1
    if m == 0:
        break
    else:
        sum += second_max
        m -= 1

print(sum)
# 답이 46으로 알맞게 나온다.

# 교재의 풀이 ('이것이 코딩테스트다 With 파이썬', 나동빈, 한빛미디어, p95)

n,m,k = map(int,input().split())
# # 자연수 n개가 주어진다. 가장 큰 수를 최대한 많이 더할수록 큰 수가 나올 것이니 큰 수부터 찾자.
data = list(map(int,input().split()))
data.sort()
first_max = data[-1]
# # 가장 큰 수를 연속해서 더할 수 있는 횟수가 숫자가 더해지는 횟수보다 작다는 전제가 있으므로 두번째 큰 수도 찾자.
second_max = data[-2]
# [66656665]가 가장 클 것이니 여기서의 반복되는 수열은 [6665]이므로 수열의 길이는 최대횟수에 1을 더한 4이다. 즉 k+1
# k+1 에다가 k를 곱해줘야 6을 3번 곱한 값을 몫만큼 곱해준다라는 말이 된다. 빼먹지 않도록 조심.
count = int(m / (k+1)) * k
count += m % (k+1) 

sum = 0
sum += count * first_max
sum += (m - count) * second_max
print(sum)
