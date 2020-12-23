def solution(A):
    N= len(A)
    M = 0
    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)
    count = [0] * (M + 1)
    for i in range(N):
        count[A[i]] += 1
    dp = [-1] * (S + 1)
    dp[0] = 0
    for a in range(1, M + 1):
        if count[a] > 0:
            for j in range(S):
                if dp[j] >= 0:
                    dp[j] = count[a]
                elif (j >= a and dp[j - a] > 0):
                    dp[j] = dp[j - a] - 1
    res = S
    for i in range(S // 2 + 1):
      if dp[i] >= 0:
        res = min(res, S - 2 * i)
    return res
