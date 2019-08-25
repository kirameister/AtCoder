N, T, *V = map(int, open(0).read().split())
wa = 0
prev = 0
for i in range(N):
  if(V[i] - prev < T):
    wa += V[i] - prev
  else:
    wa += T
  prev = V[i]
  pass
wa += T
print(wa)