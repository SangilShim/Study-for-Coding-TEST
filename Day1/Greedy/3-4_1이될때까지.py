# 어떠한 수 n이 1이 될때까지 1을 빼거나 k로 나누는데, 그 횟수가 가장 적은 경우(greedy)를 찾는 것

# 풀이 1 (오답)
# while 과 for의 사용에 대해 아직 미숙하다. for문을 보면 n-1까지 반복한다는 것은 결국 while True와 같은 말이므로 입력을 해도 출력 자체가 되지 않았다.
n , k = map(int, input().split())
count = 0
while True:
    for i in range(n-1):
        if n % k != 0:
            n -= 1
            count += 1
        elif n % k == 0:
            n = n // k
            count += 1
    if n == 1:
        break

print(count)


# 풀이 2 (정답) 
# for문을 제거하고 while문으로 반복하면서 조건도 변경해보았다. if n == 1이라는 조건을 뒤에다가 놓으면 n == 0 이 되어도 계속 반복될 것이므로 n == 0 을 첫번째 조건으로 두었다.
n , k = map(int, input().split())
count = 0
while True:
    if n == 1:
        break
    elif n % k != 0:
        n -= 1
        count += 1
    else:
        n = n // k
        count += 1
print(count)

# 교재 풀이 ('이것이 코딩테스트다',나동빈, 한빛미디어, p101)
n ,k = map(int, input().split())
count = 0
while n >= k:
    while n % k != 0:
        n -= 1
        count += 1
    n //= k
    count += 1
while n > 1:
    n -= 1
    count += 1
print(count)
