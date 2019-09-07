N,M, *V = map(int, open(0).read().split())
P = V[0::2]
Y = V[1::2]

table = dict()

for i in range(len(P)):
  if(P[i] in table):
    table[P[i]].append(Y[i])
  else:
    table[P[i]] = []
    table[P[i]].append(Y[i])

for key in table.keys():
  table[key] = sorted(table[key])

sr_table = dict()

for key in table.keys():
  sr_table[key] = dict()
  for i in range(len(table[key])):
    sr_table[key][table[key][i]] = i+1

for i in range(len(P)):
  order = sr_table[P[i]][Y[i]]
  pre  = '{:0=6}'.format(P[i])
  post = '{:0=6}'.format(order)
  print(str(pre) + str(post))