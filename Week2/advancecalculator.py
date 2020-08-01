# i used float because i want the user to enter only numbers
 num1 = float(input("Enter your first number: ")) 
 opr = input("Enter operator: ") 
 num2 = float(input("Enter your second number: "))
  if opr == "-" : 
      print(num1 - num2) 
  elif opr == "+" :
       print(num1 + num2) 
  elif opr == "/" :
       print(num1 / num2)
 elif opr == "*" :
      print(num1 * num2)
 else:
      print("You have entered an invalid operator")