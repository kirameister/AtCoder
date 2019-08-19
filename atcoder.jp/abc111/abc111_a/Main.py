v = list(input())
v2 = list()

for i in v: 
  if(i == '9'):
    v2.append('1')
  else:
    v2.append('9')
    
print("".join(v2))