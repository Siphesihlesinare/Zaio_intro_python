pi = 0
acc = 100000

for a in range(0,acc):
  pi += ((4.0*(-1)**a)/(2*a+1))
  pi = round(pi,3)
  
user = float(input("Enter the redius: "))
area = pi*(user**2)
print("The approximation of pi : ",pi)
print("Area: ",area)
  
