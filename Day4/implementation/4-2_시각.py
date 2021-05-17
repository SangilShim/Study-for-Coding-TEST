# 시각 문제 : 시각의 hh:mm:ss 의 각 원소 중 3이 포함되면 카운팅 해주는 문제이다.

# 내 풀이 (정답) : 노가다로 풀었지만 논리는 맞았다.

n = int(input())
big = [0,1,2,3,4,5]
small = [0,1,2,3,4,5,6,7,8,9]

count = 0

for a in big:
    if a == 3:
        count += len(small) * len(big) * len(small)
    else:
        for b in small:
            if b == 3:
                count += len(big) * len(small)
            else:
                for c in big:
                    if c == 3:
                        count += len(small)
                    else:
                        for d in small:
                            if d == 3:
                                count += 1
                            else:
                                pass
if n < 3:
    result = (n+1) * (count)
elif 3 <= n and n < 13: 
    result = ((n) * (count)) + (len(big) * len(small) * len(big) * len(small))
elif 13 <= n and n < 23:
    result = ((n-1) * (count)) + ((len(big) * len(small) * len(big) * len(small)) * 2)
else:
    result = ((n-2) * (count)) + ((len(big) * len(small) * len(big) * len(small)) * 3)

print(result)

# 교재 풀이 ('이것이 코딩테스트다', 나동빈, 한솔미디어, p114)
# range(60)으로 1에서 59분까지 하면 3을 어떻게 찾아낼 수 있을까 생각했는데, str으로 변환해준 후 3문자열을 찾아내는 노하우를 알았다.
h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
