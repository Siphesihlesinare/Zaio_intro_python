num = int(input("Enter number: "))
if (num > -6) and (num < 2): # used and in this function so that
     for i in range(num, num+41):
         num = num + 7  # this adds 7 on top of each number the loop goes to
         print("{0:2}".format(str("[3]")), num) # {} is used to specify the field wiedth and .format
# what should be inside that will be printed
else:
    print("Wrong number enter a new one!")
