# Q5. 볼링공 고르기 문제 : 볼링공이 총 n개, 무게는 1~m의 형태로 주어져있을 때, 최대한 만들 수 있는 (greedy) 행렬의 수 구하기 (단, 행과 열의 수는 달라야 한다)

# 내 풀이 (정답 : 19분 30초) : 논리가 완벽하다고 생각한다. for문을 조금 더 이해할 수 있었던 문제다.

n, m = map(int, input().split())
weight = list(map(int, input().split()))

count = 0
for i in range(len(weight)):
    k = weight[i+1:]
    for j in k:
        if weight[i] == j:
            pass
        else:
            count += 1
print(count)

# 교재의 풀이 ('이것이 코딩테스트이다', 나동빈, 한빛미디어, p513) : (5/15) 난해한 부분이 많다.
n , m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] *  11 # (5/15) 1부터 10인데 왜 11개나 만드는 걸까?
for x in data:
  # 각 무게에 해당하는 볼링공의 개수 카운트
  array[x] += 1

result = 0

for i in range(1,m+1):
  n -= array[i] # 무게가 i인 볼링공의 개수(a가 선택할 수 있는 개수) 제외
  result += array[i] * n #b가 선택하는 경우의 수와 곱하기
 
print(result)
