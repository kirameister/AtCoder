N,K,Q,*A = map(int, open(0).read().split())

deduc = [0]*N
for i in range(Q):
    deduc[A[i]-1] += 1

#print(deduc)
for i in range(N):
    if(K + ( deduc[i]  -Q ) > 0):
        print('Yes')
    else:
        print('No')


