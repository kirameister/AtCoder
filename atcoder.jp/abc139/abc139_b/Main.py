A,B = map(int, open(0).read().split())
MAX = 20
plug = 1
if(B <= 1):
  print(0)
  exit()
for i in range(MAX):
  plug -= 1
  plug += A
  if(plug >= B):
    print(i+1)
    break
    exit()

