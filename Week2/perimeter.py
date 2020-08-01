w_1 = float(input("Enter first weight: ")) 
h_1 = float(input("Enter first height: "))
w_2 = float(input("Enter second weight: "))
h_2 = float(input("Enter second height: "))
price = float(input("Enter price per meter: "))
perimeter = (w_1 + h_1 + w_2 + h_2) # how to calculate a perimeter

print("The total fence required is =  " , perimeter , " meters")
total=( (w_1 * price) + (h_1 * price) + (w_2 * price) + (h_2 * price))
print( "The total is: R" ,total)

