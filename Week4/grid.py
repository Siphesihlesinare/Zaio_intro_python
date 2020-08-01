n = int(input("Enter the number: ")) # my variable

if -6 < n and n < 2: # if statement for the requerments for the  number
    for x in range(n, 38 - (n < -4), 7): # for loop to the range on where it should start and end
        for y in range(x,  x + 7):
            print("{0:2}".format(y), end=" ")
        print()
else:
  print("Wrong number")