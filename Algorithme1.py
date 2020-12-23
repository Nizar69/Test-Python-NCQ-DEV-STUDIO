def solution(N,A):
  s = [0]*len(A)
  for i in range (len(A)) :
    if(A[i]>=1) and (A[i]<=N) :
      s[A[i]-1]+=1
    elif (A[i] == N+1):
      
      ma = max(s)
      s = [ma]*N

  return s
