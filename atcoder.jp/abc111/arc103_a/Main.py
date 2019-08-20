from collections import defaultdict

n = int(input())
v = list(map(int, input().split(' ')))

odd = defaultdict(int)
even = defaultdict(int)
al = defaultdict(int)

for i in range(len(v)):
  al[v[i]] += 1
  if(i % 2 == 0): # even
    even[v[i]] += 1
  else: # odd
    odd[v[i]] += 1

if(len(al) == 1):
  print(n // 2)
  exit()

even_sorted = sorted(even.items(), key=lambda x: x[1], reverse=True)
odd_sorted = sorted(odd.items(), key=lambda x: x[1], reverse=True)

#print(even_sorted[0:4])
#print(odd_sorted[0:4])


if(len(even_sorted) == 1): # what if either of them had only one uniq num..
  if(odd_sorted[0][0] == even_sorted[0][0]):
    print(n - odd_sorted[1][1]  - even_sorted[0][1])
  else:
    print(n - odd_sorted[0][1] - even_sorted[0][1])
elif(len(odd_sorted) == 1):
  if(odd_sorted[0][0] == even_sorted[0][0]):
    print(n - even_sorted[1][1] - odd_sorted[0][1])
  else:
    print(n - odd_sorted[0][1] - even_sorted[0][1])


else: # both of them have more than 1 uniq num..
  if(odd_sorted[0][0] == even_sorted[0][0]):
    if(odd_sorted[0][1] == even_sorted[0][1]):
      if(odd_sorted[1][1] < even_sorted[1][1]):
        print(n - odd_sorted[0][1] - even_sorted[1][1])
      else:
        print(n - odd_sorted[1][1] - even_sorted[0][1])
    elif(odd_sorted[0][1] < even_sorted[0][1]): # odd to be changed (even stays)
      print(n - odd_sorted[1][1] - even_sorted[0][1])
    else:
      print(n - odd_sorted[0][1] - even_sorted[1][1])
  else: # both has more than 1 uniq num, and most freq values aren't the same
    print(n - odd_sorted[0][1] - even_sorted[0][1])

