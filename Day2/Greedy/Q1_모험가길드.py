# 모험가길드 : 공포도를 가진 팀원들을 가지고 팀을 꾸리는데, 팀의 인원은 공포도가 가장 큰 팀원의 공포도 이상이어야 한다.

# 나의 풀이 (19분 30초 : 정답)
# 정답이긴 하지만 논리가 틀려 분명히 예외가 있을 것 같다. 그런데 예외를 못찾고있다.(5/15)
# 나는 데이터를 정렬한 후에 가장 끝 수(큰 수)만큼의 팀원을 잘라내고 그 남은 팀원으로 이걸 반복하다가 팀원의 수가 마지막 수보다 작을 경우에는 멈추는 논리를 세웠다.
# 그런데 생각해보니 이렇게 코드를 짜면 마지막 가장 큰 수가 계속 팀에 머물게 되므로 틀린 논리이다.
n = int(input())
data = list(map(int, input().split()))
data.sort()
count = 0
for i in range(len(data)):
    first = data[-1]
    data = data[(first-1):]
    count += 1
    if len(data) < data[-1]:
        break
print(count)

# 교재의 풀이 ('이것이 코딩테스트다', 나동빈, 한빛미디아, p506)
# 나와는 다르게 2개의 요소를 카운트하였고(팀원, 팀의 수) 팀원의 수가 공포도 이상일 때 팀의 수를 늘려주는 방식의 논리를 펼쳤다. 
n = int(input())
data = list(map(int, input().split()))
data.sort()

team = 0
member = 0
for i in data:
    member += 1
    if member >= i:
        team += 1
        member = 0
print(team)
