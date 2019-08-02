chars = sorted(list(input()))
#print(chars)
uniq = set(chars)
if(len(uniq) != 2):
  print("No")
elif(chars[1] != chars[2]):
  print("Yes")
else:
  print("No")