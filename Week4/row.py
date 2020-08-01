number = int(input("Enter number ")) # variable

if (number > -6) and (number < 93):

    for i in range(number, number + 7):

        print('{0:2}'.format(str('[2]' + str(i))), end='')
else:
    print("Wrong number")
