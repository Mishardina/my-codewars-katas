#https://www.codewars.com/kata/5b61e9306d0db7d097000632

N = 1800
DP = [[0] * (N + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    DP[n][1] = 1
    for k in range(2, n + 1):
        DP[n][k] = DP[n - 1][k - 1] + k * DP[n - 1][k]

def combs_non_empty_boxesII(n):
    total  = sum(DP[n])
    opt, k = max((DP[n][x], x) for x in range(1, n + 1))
    return [total, opt, k]