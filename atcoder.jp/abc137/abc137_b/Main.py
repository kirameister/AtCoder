v = list(map(int, input().split()))

kagen = v[1] - v[0] + 1
jogen = v[1] + v[0]
ans = list()
for i in range(kagen, jogen):
  ans.append(str(i))
print(" ".join(ans))