# 숫자카드게임 행렬 형식으로 입력되면 각 행에서 가장 작은 수를 뽑고 다른 열과 비교하여 가장 큰 수를 뽑아내는 게임이다.


# 첫번째 풀이 (오답)
# 첫번째 입력예시를 봤을 때 (3,3)의 경우만 생각하여 풀이하였기 때문에 다른 (2,4)와 같은 다른 입력에는 오류가 생겼다.
n, m = map(int, input().split())
data_1 = list(map(int, input().split()))
data_1.sort()
data_2 = list(map(int, input().split()))
data_2.sort()
data_3 = list(map(int, input().split()))
data_3.sort()

small_1 = data_1[0]
small_2 = data_2[0]
small_3 = data_3[0]

if (small_1 > small_2) and (small_1 > small_3):
    print(small_1)
elif (small_2 > small_1) and (small_2 > small_3):
    print(small_2)
else:
    print(small_3)
    
    
# 두번째 풀이 (정답)
# 역시나 반복문을 써야했다. 이것저것 잔가지들을 다듬어가는 과정을 교재의 답과 비교하여 줄여나가도록 해야겠다.

n , m = map(int, input().split())
Max = []
for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    a = data[0]
    Max.append(a)
Max.sort()
result = Max[-1]
print(result)

# 교재 풀이 (1) ('이것이 코딩테스트다',나동빈, 한빛미디어, p98)
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
