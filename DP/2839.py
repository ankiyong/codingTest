limit = 5000
N = int(input())
dp = [limit] * 5001

dp[3],dp[5] = 1,1

for i in range(6,N+1):
    dp[i] = min(dp[i-3],dp[i-5]) + 1


if dp[N] >= limit:
    print(-1)
else:
    print(dp[N])