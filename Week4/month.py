month = input("Enter your month :")
day = input("Enter your day :")

if month == "April" :
  days = 30 
if month == "May" :
  days = 31
if month == "June" :
  days = 30
if month == "March" :
  days = 31
if month == "August" :
  days = 31
if month == "September" :
  days = 30 
if month == "October" :
  days = 31
if month == "November" :
  days = 30
if month == "January" :
   days = 31
if month == "October" :
  days = 31
if month == "July" :
  days = 31
if month == "February" :
  days = 28


DAY_B = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
blank = DAY_B.index(day)

print("Mo Tu We Th Fr Sa Su")

for i in range(blank):
  print("  ", end= ' ' )

for i in range(days) :
  print("%2d" % (i+1), end= ' ' )
  if (i + blank) % 7 == 6:
    print()