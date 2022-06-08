from sys import stdin

s1 = stdin.readline().strip()
s2 = stdin.readline().strip()

dp = [0] * len(s2)
for i in range(len(s1)):
    max_val = 0
    for j in range(len(s2)):
        # 가장 큰 값을 갱신한다
        if max_val < dp[j]:
            max_val = dp[j]

        # 문자열 s2의 j번째 원소를 추가하면 부분수열의 길이가 1만큼 증가한다
        # 가장 큰 값을 갱신하고나서 그 다음 인덱스부터 dp값을 갱신하는 것이 맞다
        elif s1[i] == s2[j]:  
            dp[j] = max_val + 1


print(max(dp))