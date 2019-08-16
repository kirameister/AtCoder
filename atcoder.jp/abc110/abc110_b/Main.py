(n, m, x, y) = list(map(int, input().split()))
xs = list(map(int, input().split()))
ys = list(map(int, input().split()))

xs.sort()
ys.sort()

#print(n, m, x, y)
#print(xs)
#print(ys)

if(xs[-1] < x):
  xs[-1] = x
if(y < ys[0]):
  ys[0] = y

z = ys[0]
if(z <= xs[-1]):
  print("War")
elif(x < z and z <= y):
  print("No War")
else:
  print("War")