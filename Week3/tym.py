hour = float(input("Enter hour: " )) 
mino = float(input("Enter minutes: " ))
sec = float(input("Enter sec: " ))

if (hour > -1) and (hour < 25) and (mino > -1) and (mino <61)   and (sec > -1) and (sec < 61):

  print("your time is valid")

else:
   print("Your time in invalid")