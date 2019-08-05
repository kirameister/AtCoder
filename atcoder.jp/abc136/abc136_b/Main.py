a = input()
su = 0
for i in range(1, int(a)+1):
    li = list(str(i))
    if(len(li) % 2 == 0): # digit is even..
        continue
    #print(i)
    su = su + 1
print(su)
