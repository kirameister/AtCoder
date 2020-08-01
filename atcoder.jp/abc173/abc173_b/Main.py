AC = 0
WA = 0
TLE = 0
RE = 0

N = int(input())
for i in range(N):
  a = input()
  if(a == 'AC'):
    AC+=1
  elif(a == 'WA'):
    WA+=1
  elif(a == 'TLE'):
    TLE+=1
  else:
    RE+=1

print('AC x ' + str(AC))
print('WA x ' + str(WA))
print('TLE x ' + str(TLE))
print('RE x ' + str(RE))






