N,T,A,*H = map(int, open(0).read().split())
B=[]
ans = -1;
minim = 10000000000000000;
for i in range(N):
  B.append(T - H[i] * 0.006)
for i in range(N):
  if(abs(B[i]-A) < minim):
    ans = i+1
    minim = abs(B[i]-A)

print(ans)