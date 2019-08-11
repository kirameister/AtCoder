values = list(map(int, input().split(' ')))
AplusB = values[0] + values[1]
AminusB = values[0] - values[1]
AtimesB = values[0] * values[1]
print(max([AplusB, AminusB, AtimesB]))