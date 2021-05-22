# 문자열압축, 같은 거는 줄여서 숫자붙여주기 슬라이싱을 제일 적게하는 것으로 고르는 문제이다.

# 풀이실패

# 교재풀이 ('이것이 코딩테스트이다', 나동빈, 한솔미디어, p518)
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count)증가
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                # 다시 상태 초기화 하는 목적인데 이유를 모르겠다
                prev = s[j:j + step]
                count = 1
        # 남아 있는 문자열에 대해서 처리한다고 했는데, 이것도 위에서 했는데 왜 또하는지 모르겠다
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
