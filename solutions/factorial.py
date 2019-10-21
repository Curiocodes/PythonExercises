def fact(x):
  f = 1
  for i in range(1,x+1):
    f*=i
  return f

x = int(input("Enter number :"))
print(fact(x))
