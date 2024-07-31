num = int(input("num: "))
k = num
if num < 0:
  num =- k
s = 0
while(num > 0):
  s += num
  num -=1
else:
  if k<0:
    print("sum:",-(s))
  else:
    print("sum:", s)
  
