N,*H = map(int, open(0).read().split())
point = 0
max_count = 0

for i in range(N-1):
    if(H[i] < H[i+1]):
        if((i-point) > max_count):
            max_count = i-point
        point = i+1
if((N-point-1) > max_count):
  max_count = N-point-1

print(max_count)

