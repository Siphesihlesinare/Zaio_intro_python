num1 = int(input("Enter the start point: "))
num2 = int(input("Enter the end point: "))

for i in range(num1, num2,):
        a = True
        if(str(i) == str(i)[::-1]):
            if(i>2):
                for num1 in range(2,i):
                    if(i%num1==0):
                        a = False
                        break
                if a:
                    print(i)
                    