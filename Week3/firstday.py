firstyear=int(input("Enter the first year:\n"))
secondyear=int(input("Enter the second year:\n"))

def R(n,m):
    return (n%m)



for index in range(firstyear,secondyear+1):
    index=int(index)

    a=1+5*R(index-1,4)
    b=4*R(index-1,100)
    c=6*R(index-1,400)
    d=a+b+c

    day=R(d,7)

    day=int(day)
    if day==0:
        output="Sunday"
    elif day==1:
        output="Monday"
    elif day==2:
        output="Tuesday"
    elif day==3:
        output="Wednesday"
    elif day==4:
        output="Thrusday"
    elif day==5:
        output="Friday"
    elif day==6:
        output="Saturday"

    print("The 1st of January "+str(index)+" falls on a "+str(output))