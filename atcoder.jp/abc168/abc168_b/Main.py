i = input()
i2 = input()

l2 = list(i2)
if(len(l2) <= int(i)):
  print(i2)
else:
  print("".join(l2[0:int(i)])+'...')