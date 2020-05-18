i = input()
i2 = list(i)[-1]
if(i2 == '3'):
  print("bon")
elif(i2 in ('0' , '1' , '6' , '8')):
  print("pon")
else:
  print("hon")