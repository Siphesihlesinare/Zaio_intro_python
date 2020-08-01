import math #used math iport the math library
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))# math.sqrt is the function to find a squar root in th math library

print("The area of a triangle with side of length " , a ,  " and " , b , " and " , c , " is " , area)