#!/usr/bin/env python3

(N, K) = map(lambda x: int(x), input().split(' '))
AL = [False for i in range(int(N))]
#print(AL)

for i in range(K):
    d = int(input())
    A = [i for i in map(lambda x: int(x) -1, input().split(' '))]
    for i in A:
        AL[i] = True
#print(AL)
print(len([1 for x in AL if x==False]))


