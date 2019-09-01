s,d = map(str, open(0).read().split())
ss = list(s)
dd = list(d)
a = 0
for i in range(len(ss)):
  if(ss[i] == dd[i]):
    a += 1
    
print(a)