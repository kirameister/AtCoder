N, T, *V = map(int, open(0).read().split())
cs = V[0::2]
ts = V[1::2]
ans = 1001

for i in range(N):
  if(ts[i] > T):
    continue
  if(cs[i] < ans):
    ans = cs[i]

if(ans == 1001):
  print("TLE")
else:
  print(ans)