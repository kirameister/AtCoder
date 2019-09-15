S = list(open(0).read())
odd  = S[0::2]
even = S[1::2]

uo = set(odd)
ue = set(even)

if('L' in uo or 'R' in ue):
  print('No')
else:
  print('Yes')

