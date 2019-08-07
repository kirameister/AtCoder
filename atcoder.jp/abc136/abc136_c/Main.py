index = int(input())
values = list(map(int, input().split()))

for i in range(index):
  if(i == 0 and values[i] > 0):
    values[i] = values[i] -1
    continue
  if(values[i] > values[i-1]):
    values[i] = values[i] - 1
#print(values)
flag = "Yes"
for i in range(index):
  if(i == 0):
    continue
  if(values[i] < values[i-1]):
    flag = "No"

print(flag)