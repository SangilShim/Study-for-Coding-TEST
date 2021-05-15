# 만들 수 없는 금액 : 알고리즘을 이해하기에 어려움이 많았다. 교재를 참고해보니 타겟을 1로 정하고 1부터 하나씩 확인해 보는 식으로 알고리즘을 짰다. 잔돈 문제와 다른 것은 동전이 한정적이라는 것.
# 잔돈 문제에서는 큰 단위의 금액부터 카운트 한 반면에 여기서는 작은 단위부터 조합을 생각해야 한다.

# 내 풀이 - 실패

#교재의 풀이 ('이것이 코딩테스트다', 나동빈, 한빛미디어, p509)
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x
print(target)
