#!/usr/bin/env python3

(N, M) = map(lambda x: int(x), input().split(' '))
H = [i for i in map(lambda x: int(x), input().split(' '))]
dest_max = [0] * len(H)

for i in range(M):
    (a, b) = map(lambda x: int(x), input().split(' '))
    dest_max[a-1] = max(dest_max[a-1], H[b-1])
    dest_max[b-1] = max(dest_max[b-1], H[a-1])

#print(H)
#print(dest_max)
print(len([1 for i in range(len(H)) if H[i] > dest_max[i] ]))


