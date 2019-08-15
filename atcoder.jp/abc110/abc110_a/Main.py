v = list(map(int, input().split()))

v.sort(reverse=True)
print(v[0] * 10 + v[1] + v[2])