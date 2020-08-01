import random
def passwordgenerator():
  lc=['a', 'b' , 'c' , 'd']
  uc=['A','B' ,'C' , 'D']
  spcl =['@', '#' , '?' , '&']
  num = ['1', '2' , '3' , '4' , '5' ]

password = random.choice(lc) + random.choice(
  uc) + random.choice(spcl) + random.choice(num) 

password = password + password + password + password


  return password
  
